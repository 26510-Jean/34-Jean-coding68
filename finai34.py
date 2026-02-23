# 1. ติดตั้ง Library ที่จำเป็น
!pip install gradio pytz -q

import gradio as gr
from datetime import datetime
import pytz

# --- ฟังก์ชันเช็คเวลาไทย (Asia/Bangkok) ---
def check_alarm(user_name, target_time, subject):
    try:
        # ดึงเวลาปัจจุบันของประเทศไทย
        tz_thai = pytz.timezone('Asia/Bangkok')
        now_thai = datetime.now(tz_thai).strftime("%H:%M")
        
        if not user_name or not target_time or not subject:
            return "✨ กรุณากรอกข้อมูลให้ครบก่อนนะคะ"
        
        # เปรียบเทียบเวลา
        if now_thai == target_time:
            return f"ALARM_NOW:ได้เวลาทำวิชา {subject} แล้วค่ะคุณ {user_name}! 💖 อย่าลืมการบ้านนะคะ"
        
        return f"🕒 เวลาไทยตอนนี้: {now_thai} | ⏳ รอแจ้งเตือนตอน: {target_time}"
    except:
        return "⚠️ รูปแบบเวลาไม่ถูกต้อง (กรุณาใช้ HH:MM)"

# --- ปรับแต่งหน้าตา (Dark Pink Theme) ---
custom_css = """
body { background-color: #0b0f19; }
.gradio-container { background-color: #0b0f19 !important; border: none !important; }
.pink-banner { 
    background: linear-gradient(90deg, #D81B60 0%, #880E4F 100%); 
    padding: 20px; border-radius: 15px; text-align: center; color: white;
    margin-bottom: 20px; box-shadow: 0 4px 15px rgba(216, 27, 96, 0.4);
}
.input-box { border: 1px solid #D81B60 !important; background-color: #1a1a1a !important; color: white !important; }
.status-box { border: 2px dashed #D81B60 !important; background-color: #251017 !important; color: #ff80ab !important; }
button.primary { background: #D81B60 !important; border: none !important; }
button.primary:hover { background: #AD1457 !important; }
"""

with gr.Blocks(css=custom_css) as demo:
    # Header
    gr.HTML("""
        <div class='pink-banner'>
            <h1 style='color: white; margin: 0;'>🌸 ระบบแจ้งเตือนการบ้านสุดคิวท์ (Stable Edition) 🌸</h1>
            <p style='color: #f8bbd0; margin: 5px 0 0 0;'>แม่นยำตามเวลาจริงประเทศไทย 🇹🇭</p>
        </div>
    """)
    
    with gr.Row():
        name_in = gr.Textbox(label="ชื่อผู้ใช้", placeholder="กรอกชื่อของคุณ...", value="เพื่อนรัก")
        # ดึงเวลาปัจจุบันมาโชว์เป็นตัวอย่าง
        tz_thai = pytz.timezone('Asia/Bangkok')
        current_t = datetime.now(tz_thai).strftime("%H:%M")
        time_in = gr.Textbox(label="เวลาแจ้งเตือน (HH:MM)", value=current_t)
    
    subject_in = gr.Textbox(label="วิชา", placeholder="รายวิชาที่ต้องทำวันนี้...")
    
    btn_start = gr.Button("🚀 เริ่มระบบแจ้งเตือน", variant="primary")
    
    # ส่วนแสดงสถานะ
    status_display = gr.Label(
        value="กดปุ่มเพื่อเริ่มระบบ...", 
        label="สถานะการทำงาน",
        elem_classes=["status-box"]
    )

    # --- วิธีแก้ SyntaxError: ต้องระบุวินาทีใน Timer ---
    timer = gr.Timer(1) 
    timer.tick(check_alarm, [name_in, time_in, subject_in], status_display)

    # --- วิธีแก้ TypeError: เปลี่ยนจาก _js เป็น js (Gradio 5.0+) ---
    status_display.change(None, status_display, None, js="""
        (msg) => {
            if (msg && msg.includes('ALARM_NOW')) {
                const message = msg.replace('ALARM_NOW:', '');
                // เล่นเสียงแจ้งเตือน
                var audio = new Audio('https://actions.google.com/sounds/v1/alarms/beep_short.ogg');
                audio.play();
                // เด้ง Alert
                alert('🔔 แจ้งเตือน: ' + message);
            }
        }
    """)

# รันหน้าเว็บ (share=True เพื่อให้ได้ลิงก์เด้งไปหน้าเว็บใหม่)
demo.launch(share=True)
