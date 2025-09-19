import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

def to_rgb(image):
    if len(image.shape) == 2:
        return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def gaussian_blur(image):
    return cv2.GaussianBlur(image, (15, 15), 0)

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def rotate(image, angle=30):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, matrix, (w, h))

def translate(image, tx=100, ty=70):
    h, w = image.shape[:2]
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, matrix, (w, h))

def shear(image, shearX=-0.15, shearY=0):
    h, w = image.shape[:2]
    matrix = np.float32([[1, shearX, 0], [0, 1, shearY]])
    return cv2.warpAffine(image, matrix, (w, h))

def normalize(image):
    # Normalize each channel to 0-255 and merge
    b, g, r = cv2.split(image)
    b_norm = cv2.normalize(b, None, 0, 255, cv2.NORM_MINMAX)
    g_norm = cv2.normalize(g, None, 0, 255, cv2.NORM_MINMAX)
    r_norm = cv2.normalize(r, None, 0, 255, cv2.NORM_MINMAX)
    return cv2.merge((b_norm, g_norm, r_norm)).astype(np.uint8)

def edge_detection(image):
    image_rgb = to_rgb(image)
    return cv2.Canny(image_rgb, 100, 700)

def log_transform(image):
    # Apply log transform to each channel and return RGB
    img_rgb = to_rgb(image)
    c = 255 / (np.log(1 + np.max(img_rgb)))
    log_transformed = c * np.log(1 + img_rgb.astype(np.float32))
    return np.array(log_transformed, dtype=np.uint8)

def gamma_correction(image, gamma=1.2):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gamma_corrected = np.array(255 * (img_gray / 255) ** gamma, dtype='uint8')
    return gamma_corrected

def contrast_stretch(image):
    def pixelVal(pix, r1, s1, r2, s2):
        if (0 <= pix and pix <= r1):
            return (s1 / r1) * pix
        elif (r1 < pix and pix <= r2):
            return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
        else:
            return ((255 - s2) / (255 - r2)) * (pix - r2) + s2
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    r1, s1, r2, s2 = 70, 0, 140, 255
    pixelVal_vec = np.vectorize(pixelVal)
    return pixelVal_vec(img_gray, r1, s1, r2, s2).astype(np.uint8)

def hist_equalization(image):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.equalizeHist(img_gray)

st.title('OpenCV Image Processing App')


# --- Modern UI/UX ---
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}
.stButton>button {
    background: linear-gradient(90deg, #6366f1 0%, #06b6d4 100%);
    color: white;
    border-radius: 8px;
    font-weight: 600;
    padding: 0.5em 2em;
}
.stSelectbox>div>div {
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

with st.container():
    st.header('Image Processing Playground 🖼️')
    st.caption('Select a filter, adjust parameters, and apply to your image!')

uploaded_file = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png', 'webp'])

functions = [
    'None',
    'Gaussian Blur',
    'Grayscale',
    'Rotate',
    'Translate',
    'Shear',
    'Normalize',
    'Edge Detection',
    'Log Transform',
    'Gamma Correction',
    'Contrast Stretching',
    'Histogram Equalization'
]

selected_function = st.selectbox('Select a filter (no filter applied by default)', functions)

params = {}
if selected_function == 'Gaussian Blur':
    params['ksize'] = st.slider('Blur Amount', 0, 100, 15, 1)
elif selected_function == 'Rotate':
    params['angle'] = st.slider('Rotation Angle', -180, 180, 30, 1)
elif selected_function == 'Translate':
    params['tx'] = st.slider('Translate X', -200, 200, 100, 1)
    params['ty'] = st.slider('Translate Y', -200, 200, 70, 1)
elif selected_function == 'Shear':
    params['shearX'] = st.slider('Shear X', -1.0, 1.0, -0.15, 0.01)
    params['shearY'] = st.slider('Shear Y', -1.0, 1.0, 0.0, 0.01)
elif selected_function == 'Gamma Correction':
    params['gamma'] = st.slider('Gamma', 0, 100, 12, 1)



if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    col1, col2 = st.columns(2)
    with col1:
        st.image(to_rgb(image), caption='Original Image', use_container_width=True)

    result = None
    result_caption = ''
    result_channels = None

    if selected_function != 'None':
        if selected_function == 'Gaussian Blur':
            blur_val = params.get('ksize', 15)
            # Map 0-100 to odd kernel size (1-101)
            k = max(1, int(blur_val))
            if k % 2 == 0:
                k += 1
            result = cv2.GaussianBlur(image, (k, k), 0)
            result_caption = f'Gaussian Blurred (amount={blur_val})'
        elif selected_function == 'Grayscale':
            result = grayscale(image)
            result_caption = 'Grayscale'
            result_channels = 'GRAY'
        elif selected_function == 'Rotate':
            angle = params.get('angle', 30)
            result = rotate(image, angle)
            result_caption = f'Rotated ({angle}°)'
        elif selected_function == 'Translate':
            tx = params.get('tx', 100)
            ty = params.get('ty', 70)
            result = translate(image, tx, ty)
            result_caption = f'Translated (x={tx}, y={ty})'
        elif selected_function == 'Shear':
            shearX = params.get('shearX', -0.15)
            shearY = params.get('shearY', 0.0)
            result = shear(image, shearX, shearY)
            result_caption = f'Sheared (X={shearX}, Y={shearY})'
        elif selected_function == 'Normalize':
            result = normalize(image)
            result_caption = 'Normalized'
        elif selected_function == 'Edge Detection':
            result = edge_detection(image)
            result_caption = 'Edges'
            result_channels = 'GRAY'
        elif selected_function == 'Log Transform':
            result = log_transform(image)
            result_caption = 'Log Transformed'
            result_channels = None
        elif selected_function == 'Gamma Correction':
            gamma_val = params.get('gamma', 12)
            # Map 0-100 to 0.1-5.0 (avoid 0)
            gamma = max(0.1, gamma_val / 20)
            result = gamma_correction(image, gamma)
            result_caption = f'Gamma Corrected (gamma={gamma:.2f})'
            result_channels = 'GRAY'
        elif selected_function == 'Contrast Stretching':
            result = contrast_stretch(image)
            result_caption = 'Contrast Stretched'
            result_channels = 'GRAY'
        elif selected_function == 'Histogram Equalization':
            result = hist_equalization(image)
            result_caption = 'Histogram Equalized'
            result_channels = 'GRAY'

    with col2:
        if result is not None:
            if result_channels == 'GRAY':
                st.image(result, caption=result_caption, use_container_width=True, channels='GRAY')
                img_pil = Image.fromarray(result)
            else:
                st.image(to_rgb(result), caption=result_caption, use_container_width=True)
                img_pil = Image.fromarray(to_rgb(result))
        else:
            st.info('Result will appear here after you select a filter.')

    # Center the download button below both images, if result exists
    if result is not None:
        buf = io.BytesIO()
        img_pil.save(buf, format='PNG')
        byte_im = buf.getvalue()
        btn_col1, btn_col2, btn_col3 = st.columns([1,2,1])
        with btn_col2:
            st.download_button(
                label='Download Result Image',
                data=byte_im,
                file_name='processed_image.png',
                mime='image/png'
            )
    if selected_function == 'None':
        st.info('No filter selected. Please choose a filter.')
 