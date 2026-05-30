import streamlit as st
import os
import base64

# 1. 페이지 설정 및 와이드 모드 필수 활성화
st.set_page_config(page_title="나노바이오의약학실험실", layout="wide")

# 이미지 저장을 위한 디렉토리 생성
UPLOAD_DIR = "saved_images"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# --- 📁 파일 저장 및 로드용 헬퍼 함수 ---
def save_uploaded_file(uploaded_file, filename):
    """업로드된 파일을 로컬 디렉토리에 저장"""
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filepath

def get_image_base64(filepath):
    """로컬 파일을 base64로 인코딩"""
    with open(filepath, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
# ----------------------------------------

# 2. 사진 및 글 데이터 수정을 위한 스트림릿 세션 상태(Session State) 초기화
main_saved_path = os.path.join(UPLOAD_DIR, "uploaded_main_bg.png")
if "main_bg" not in st.session_state:
    if os.path.exists(main_saved_path):
        st.session_state.main_bg = main_saved_path
    else:
        st.session_state.main_bg = "https://images.unsplash.com/photo-1579152249282-9f5d271b316a?q=80&w=1600"

for i in range(1, 4):
    if f"news_title_{i}" not in st.session_state:
        if i == 1: st.session_state.news_title_1 = "2026학년도 후기 입학전형 안내"
        elif i == 2: st.session_state.news_title_2 = "국제 학술대회 개최 소식"
        else: st.session_state.news_title_3 = "우수 연구성과 저널 발표"
        
    if f"news_text_{i}" not in st.session_state:
        if i == 1: st.session_state.news_text_1 = "2026학년도 후기 석사·박사 과정 입학전형 일정이 홈페이지에 공식 공지되었습니다."
        elif i == 2: st.session_state.news_text_2 = "차세대 바이오 의약학 기술 국제 심포지엄이 다가오는 전반기 본교에서 개최됩니다."
        else: st.session_state.news_text_3 = "본 연구팀의 나노입자 기반 의약학 치료 기전 논문이 국제 학술지에 게재 승인되었습니다."
        
    news_saved_path = os.path.join(UPLOAD_DIR, f"uploaded_news_{i}.png")
    if f"news_img_{i}" not in st.session_state:
        if os.path.exists(news_saved_path):
            st.session_state[f"news_img_{i}"] = news_saved_path
        else:
            if i == 1: st.session_state.news_img_1 = "https://images.unsplash.com/photo-1532187863486-abf9d39d6618?q=80&w=600"
            elif i == 2: st.session_state.news_img_2 = "https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600"
            else: st.session_state.news_img_3 = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=600"

# 3. CSS 오버라이드
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] > section:nth-child(2) {
        padding: 0px !important;
    }
    .stMain {
        max-width: 100% !important;
        width: 100% !important;
        padding: 0 !important;
    }
    .block-container {
        max-width: 92% !important;
        width: 92% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        margin: 0 auto !important;
    }
    .header-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        padding: 20px 0;
        border-bottom: 2px solid #E2E8F0;
        margin-bottom: 35px;
    }
    div[data-testid="stPopover"] > button {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
        color: #1E3A8A !important;
        font-weight: 700 !important;
    }
    .custom-card {
        background-color: white;
        border-radius: 14px;
        box-shadow: 0 4px 20px rgba(15, 23, 42, 0.05);
        overflow: hidden;
        border: 1px solid #E2E8F0;
        margin-bottom: 20px;
        width: 100%;
    }
    .custom-card img, .uploaded-img-wrapper img {
        width: 100% !important;
        height: 320px !important; 
        object-fit: cover !important;
        display: block !important;
    }
    .card-body {
        padding: 24px;
    }
    div[data-testid="stPopover"] img {
        max-width: 150px !important;
        height: auto !important;
    }
    </style>
""", unsafe_allow_html=True)

# 4. 상단 네비게이션 헤더 및 관리자 팝업 기능
header_left, header_right = st.columns([2, 3])

with header_left:
    st.markdown("""
    <div style="padding: 15px 0; font-size: 28px; font-weight: 800; color: #1E3A8A; letter-spacing: -1px; line-height:1.2;">
        나노바이오의약학실험실
    </div>
    """, unsafe_allow_html=True)

with header_right:
    menu_1, menu_2, menu_3, menu_4, menu_admin = st.columns([1, 1, 1.2, 1, 1.5])
    with menu_1: st.write("소개")
    with menu_2: st.write("커뮤니티")
    with menu_3: 
        st.link_button("연구논문", url="https://scholar.google.com/citations?hl=ko&user=hBXqv1EAAAAJ&view_op=list_works&sortby=pubdate")
    with menu_4: st.write("소식")
    
    with menu_admin:
        with st.popover("관리자 ⚙️"):
            st.markdown("### 🔐 관리자 인증")
            password = st.text_input("비밀번호를 입력하세요", type="password")
            
            if password == "020110":
                st.success("인증 성공!")
                st.markdown("---")
                st.markdown("🖼️ **메인 배너 이미지 변경**")
                main_file = st.file_uploader("메인 배너 사진 업로드", type=["jpg", "png", "jpeg"], key="main_upload")
                if main_file:
                    saved_path = save_uploaded_file(main_file, "uploaded_main_bg.png")
                    st.session_state.main_bg = saved_path
                    st.success("메인 배너가 서버에 영구 저장되었습니다!")
                
                st.markdown("---")
                st.markdown("📢 **최근 소식 콘텐츠 변경**")
                for i in range(1, 4):
                    with st.expander(f"소식 카드 {i}번 수정"):
                        new_title = st.text_input(f"카드 {i} 제목", value=st.session_state[f"news_title_{i}"])
                        new_text = st.text_area(f"카드 {i} 본문", value=st.session_state[f"news_text_{i}"])
                        st.session_state[f"news_title_{i}"] = new_title
                        st.session_state[f"news_text_{i}"] = new_text
                        news_file = st.file_uploader(f"카드 {i} 사진 업로드", type=["jpg", "png", "jpeg"], key=f"news_upload_{i}")
                        if news_file:
                            saved_news_path = save_uploaded_file(news_file, f"uploaded_news_{i}.png")
                            st.session_state[f"news_img_{i}"] = saved_news_path
            elif password != "":
                st.error("비밀번호 불일치")

st.markdown("<hr style='margin-top:-10px; margin-bottom:35px; border:1px solid #E2E8F0;'>", unsafe_allow_html=True)

# 5. 메인 히어로 배너 배포
if isinstance(st.session_state.main_bg, str) and st.session_state.main_bg.startswith("http"):
    bg_style = f"background-image: url('{st.session_state.main_bg}');"
else:
    b64_img = get_image_base64(st.session_state.main_bg)
    bg_style = f"background-image: url('data:image/jpeg;base64,{b64_img}');"

st.markdown(f"""
<div style="{bg_style} background-size: cover; background-position: center; height: 420px; border-radius: 16px; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08); margin-bottom: 50px;"></div>
""", unsafe_allow_html=True)

# 6. 최근 소식 구역
st.markdown("### 📢 최근 소식")
news_col1, news_col2, news_col3 = st.columns(3, gap="large")
cols = [news_col1, news_col2, news_col3]

for i in range(1, 4):
    with cols[i-1]:
        if isinstance(st.session_state[f"news_img_{i}"], str) and st.session_state[f"news_img_{i}"].startswith("http"):
            img_html = f'<img src="{st.session_state[f"news_img_{i}"]}">'
        else:
            card_b64 = get_image_base64(st.session_state[f"news_img_{i}"])
            img_html = f'<div class="uploaded-img-wrapper"><img src="data:image/jpeg;base64,{card_b64}"></div>'
        st.markdown(f"""
        <div class="custom-card">
            {img_html}
            <div class="card-body">
                <h4 style="margin: 10px 0 12px 0;">{st.session_state[f"news_title_{i}"]}</h4>
                <p>{st.session_state[f"news_text_{i}"]}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# 7. 문의하기 구역
st.markdown("### 📞 문의하기")
contact_col1, contact_col2, contact_col3 = st.columns(3, gap="large")
with contact_col1: st.info(f"📞 전화: 010-8474-0933")
with contact_col2: st.info(f"✉️ 이메일: kunwowo@gmail.com")
with contact_col3: st.info(f"📍 위치: 충청북도 충주시 충원대로 268")

# 8. 하단 푸터 영역
st.markdown("""
<div style="background-color: #0F172A; color: #94A3B8; padding: 40px; margin-top:50px;">
    <p>© 2026 나노바이오의약학실험실. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
