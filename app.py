import streamlit as st

# 1. 페이지 설정 및 와이드 모드 필수 활성화
st.set_page_config(page_title="나노바이오의약학실험실", layout="wide")

# 2. 사진 및 글 데이터 수정을 위한 스트림릿 세션 상태(Session State) 초기화
if "main_bg" not in st.session_state:
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
        
    if f"news_img_{i}" not in st.session_state:
        if i == 1: st.session_state.news_img_1 = "https://images.unsplash.com/photo-1532187863486-abf9d39d6618?q=80&w=600"
        elif i == 2: st.session_state.news_img_2 = "https://images.unsplash.com/photo-1582719508461-905c673771fd?q=80&w=600"
        else: st.session_state.news_img_3 = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=600"

# 3. CSS 오버라이드: 카드 내 이미지 높이를 240px -> 320px로 확장
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
        font-size: 16px !important;
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
    
    /* 🛠️ [살짝 키움] 최근 소식 이미지 영역 높이를 320px로 시원하게 확장 */
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
    with menu_1: st.markdown("<p style='font-weight:700; color:#475569; padding-top:22px; text-align:right;'>소개</p>", unsafe_allow_html=True)
    with menu_2: st.markdown("<p style='font-weight:700; color:#475569; padding-top:22px; text-align:right;'>커뮤니티</p>", unsafe_allow_html=True)
    with menu_3: st.markdown("<p style='font-weight:700; color:#475569; padding-top:22px; text-align:right;'>연구논문</p>", unsafe_allow_html=True)
    with menu_4: st.markdown("<p style='font-weight:700; color:#475569; padding-top:22px; text-align:right;'>소식</p>", unsafe_allow_html=True)
    
    with menu_admin:
        st.markdown("<div style='padding-top:18px; text-align:right;'>", unsafe_allow_html=True)
        with st.popover("관리자 ⚙️"):
            st.markdown("### 🔐 관리자 인증")
            password = st.text_input("비밀번호를 입력하세요", type="password")
            
            if password == "020110":
                st.success("인증 성공! 콘텐츠 수정 모드가 활성화되었습니다.")
                st.markdown("---")
                
                st.markdown("🖼️ **메인 배너 이미지 변경**")
                main_file = st.file_uploader("메인 배너 사진 업로드", type=["jpg", "png", "jpeg"], key="main_upload")
                if main_file:
                    st.session_state.main_bg = main_file
                
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
                            st.session_state[f"news_img_{i}"] = news_file
            elif password != "":
                st.error("비밀번호가 일치하지 않습니다.")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr style='margin-top:-10px; margin-bottom:35px; border:1px solid #E2E8F0;'>", unsafe_allow_html=True)


# 5. 메인 히어로 배너 (전체 밸런스에 맞춰 높이를 380px -> 420px로 확장)
if isinstance(st.session_state.main_bg, str):
    bg_style = f"background-image: url('{st.session_state.main_bg}');"
else:
    import base64
    bytes_data = st.session_state.main_bg.getvalue()
    b64_img = base64.b64encode(bytes_data).decode()
    bg_style = f"background-image: url('data:image/jpeg;base64,{b64_img}');"

st.markdown(f"""
<div style="
    {bg_style}
    background-size: cover;
    background-position: center;
    height: 420px; /* 🛠️ 메인 배너도 살짝 확장 */
    border-radius: 16px;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
    margin-bottom: 50px;
"></div>
""", unsafe_allow_html=True)


# 6. 최근 소식 구역
st.markdown("<h3 style='color:#0F172A; font-weight:800; margin-bottom:30px; font-size:28px; letter-spacing:-0.5px;'>📢 최근 소식</h3>", unsafe_allow_html=True)
news_col1, news_col2, news_col3 = st.columns(3, gap="large")
cols = [news_col1, news_col2, news_col3]

for i in range(1, 4):
    with cols[i-1]:
        if isinstance(st.session_state[f"news_img_{i}"], str):
            img_html = f'<img src="{st.session_state[f"news_img_{i}"]}">'
        else:
            import base64
            card_bytes = st.session_state[f"news_img_{i}"].getvalue()
            card_b64 = base64.b64encode(card_bytes).decode()
            img_html = f'<div class="uploaded-img-wrapper"><img src="data:image/jpeg;base64,{card_b64}"></div>'

        st.markdown(f"""
        <div class="custom-card">
            {img_html}
            <div class="card-body">
                <span style="color:#94A3B8; font-size:13px; font-weight:600;">📅 2026.05.29</span>
                <h4 style="margin: 10px 0 12px 0; color:#1E293B; font-weight:800; font-size:20px; letter-spacing:-0.5px;">{st.session_state[f"news_title_{i}"]}</h4>
                <p style="color:#475569; font-size:15px; line-height:1.6; margin:0;">{st.session_state[f"news_text_{i}"]}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)


# 7. 문의하기 구역
st.markdown("<h3 style='color:#0F172A; font-weight:800; margin-bottom:30px; font-size:28px; letter-spacing:-0.5px;'>📞 문의하기</h3>", unsafe_allow_html=True)
contact_col1, contact_col2, contact_col3 = st.columns(3, gap="large")

with contact_col1:
    st.markdown("""
    <div style="background-color:white; padding:35px 20px; border-radius:14px; border:1px solid #E2E8F0; text-align:center; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
        <div style="font-size:32px; margin-bottom:10px;">📞</div>
        <h5 style="margin:0 0 8px 0; color:#64748B; font-weight:700; font-size:15px;">전화 번호</h5>
        <p style="color:#1E3A8A; font-weight:800; margin:0; font-size:20px;">010-8474-0933</p>
    </div>
    """, unsafe_allow_html=True)

with contact_col2:
    st.markdown("""
    <div style="background-color:white; padding:35px 20px; border-radius:14px; border:1px solid #E2E8F0; text-align:center; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
        <div style="font-size:32px; margin-bottom:10px;">✉️</div>
        <h5 style="margin:0 0 8px 0; color:#64748B; font-weight:700; font-size:15px;">이메일 주소</h5>
        <p style="color:#1E3A8A; font-weight:800; margin:0; font-size:19px;">kunwowo@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

with contact_col3:
    st.markdown("""
    <div style="background-color:white; padding:35px 20px; border-radius:14px; border:1px solid #E2E8F0; text-align:center; box-shadow: 0 4px 15px rgba(0,0,0,0.02);">
        <div style="font-size:32px; margin-bottom:10px;">📍</div>
        <h5 style="margin:0 0 8px 0; color:#64748B; font-weight:700; font-size:15px;">연구실 위치</h5>
        <p style="color:#334155; font-size:16px; margin:0; font-weight:700;">충청북도 충주시 충원대로 268</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)

# 8. 하단 푸터 영역
st.markdown("""
<div style="background-color: #0F172A; color: #94A3B8; padding: 60px 50px; margin-left: -5%; margin-right: -5%; padding-left: 5%; padding-right: 5%;">
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 50px;">
        <div>
            <h5 style="color: white; font-weight: 800; margin-bottom: 15px; font-size:17px;">대학원</h5>
            <p style="font-size: 14px; line-height: 1.7; color:#94A3B8; margin:0;">미래를 선도하는 글로벌 교육기관<br>나노바이오의약학융합공학 전공</p>
        </div>
        <div>
            <h5 style="color: white; font-weight: 800; margin-bottom: 15px; font-size:17px;">입학안내</h5>
            <p style="font-size: 14px; line-height: 1.7; color:#94A3B8; margin:0;">전형일정 / 지원자격 / FAQ</p>
        </div>
        <div>
            <h5 style="color: white; font-weight: 800; margin-bottom: 15px; font-size:17px;">연구지원</h5>
            <p style="font-size: 14px; line-height: 1.7; color:#94A3B8; margin:0;">공동기기센터 / 학술연구비 / 시설안내</p>
        </div>
    </div>
    <div style="margin-top: 50px; padding-top: 25px; border-top: 1px solid #334155; text-align: center; font-size: 13px; color:#475569;">
        © 2026 Graduate School. All rights reserved.
    </div>
</div>
""", unsafe_allow_html=True)
