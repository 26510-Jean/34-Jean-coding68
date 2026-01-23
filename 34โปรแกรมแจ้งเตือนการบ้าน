# @title 🌸 โปรแกรมแจ้งเตือนการบ้าน (Pink Edition) 🌸
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output, Audio
from datetime import datetime
import time
import threading

# --- ส่วนของการตกแต่ง (CSS) ให้เป็นสีชมพู ---
style = """
<style>
    .widget-label { color: #D81B60 !important; font-weight: bold; }
    .widget-text { background-color: #FCE4EC; }
    .pink-header {
        background-color: #F8BBD0;
        padding: 15px;
        border-radius: 10px;
        color: #880E4F;
        text-align: center;
        font-family: 'Sarabun', sans-serif;
        margin-bottom: 20px;
        border: 2px solid #EC407A;
    }
    .alert-box {
        background-color: #FFCDD2;
        color: #C62828;
        padding: 20px;
        border: 2px dashed #B71C1C;
        border-radius: 10px;
        font-size: 18px;
        text-align: center;
        margin-top: 20px;
    }
</style>
"""

display(HTML(style))

# --- สร้าง Widget (ช่องกรอกข้อมูล) ---
header = widgets.HTML(value="<div class='pink-header'><h2>⏰ ระบบแจ้งเตือนการบ้านสุดคิวท์</h2></div>")

name_input = widgets.Text(
    description='ชื่อผู้ใช้:',
    placeholder='กรอกชื่อของคุณ',
    style={'description_width': 'initial'}
)

time_input = widgets.Text(
    description='เวลาแจ้งเตือน:',
    placeholder='เช่น 14:30',
    value=datetime.now().strftime("%H:%M"), # ใส่เวลาปัจจุบันให้ก่อน
    style={'description_width': 'initial'}
)

subject_input = widgets.Text(
    description='วิชา:',
    placeholder='กรอกชื่อวิชา',
    style={'description_width': 'initial'}
)

# ปุ่มกด (ทำให้เป็นสีชมพู)
btn_start = widgets.Button(
    description='เริ่มจับเวลา',
    button_style='danger', # สีแดง/ชมพู ใน Colab theme
    icon='check'
)

output_area = widgets.Output()

# ตัวแปรสำหรับควบคุมการทำงานของ Thread
stop_event = threading.Event()

# --- ฟังก์ชันแจ้งเตือนด้วยเสียง (เสียงกริ่ง) ---
def play_sound():
    # ใช้ Javascript เล่นเสียงเตือนใน Browser
    display(HTML("""
    <script>
        var audio = new Audio('https://upload.wikimedia.org/wikipedia/commons/d/d9/Wilhelm_Scream.ogg');
        // เปลี่ยน URL เสียงได้ถ้าต้องการเสียงอื่น (อันนี้เสียงตลกๆ Wilhelm Scream หรือเปลี่ยนเป็นเสียงกริ่ง)
        // แนะนำเสียงกริ่งสั้นๆ: https://actions.google.com/sounds/v1/alarms/beep_short.ogg
        var beep = new Audio('https://actions.google.com/sounds/v1/alarms/beep_short.ogg');
        beep.loop = true;
        beep.play();
        setTimeout(() => { beep.pause(); }, 5000); // หยุดหลังจาก 5 วินาที
    </script>
    """))

# --- ฟังก์ชันการทำงาน ---
def alarm_loop(name, target, subj):
    with output_area:
        print(f"⏳ กำลังเฝ้ารอเวลา {target} น. ... (ห้ามปิดหน้านี้นะ)")
    
    while not stop_event.is_set():
        current_time = datetime.now().strftime("%H:%M")
        
        if current_time == target:
            with output_area:
                clear_output()
                # แสดงผลแบบ HTML สีชมพู
                display(HTML(f"""
                <div class='alert-box'>
                    <h1>🔔 แจ้งเตือน! 🔔</h1>
                    <p>เวลา <b>{target}</b> น.</p>
                    <p>คุณ <b>{name}</b> ถึงเวลาเรียนวิชา <b>{subj}</b> แล้วค่ะ!</p>
                </div>
                """))
                play_sound() # เรียกฟังก์ชันเสียง
            stop_event.set() # หยุดลูป
            break
            
        time.sleep(1) # เช็คทุก 1 วินาที

def on_button_click(b):
    stop_event.clear()
    output_area.clear_output()
    
    user_name = name_input.value
    target_time = time_input.value
    subj_name = subject_input.value
    
    # ตรวจสอบว่ากรอกครบไหม
    if not user_name or not target_time or not subj_name:
        with output_area:
            print("❌ กรุณากรอกข้อมูลให้ครบทุกช่องค่ะ")
        return

    # รันลูปเช็คเวลาใน Thread แยก เพื่อไม่ให้หน้าจอค้าง
    t = threading.Thread(target=alarm_loop, args=(user_name, target_time, subj_name))
    t.start()
    
    # ปิดปุ่มชั่วคราวเพื่อกันกดซ้ำ
    btn_start.disabled = True
    time.sleep(2)
    btn_start.disabled = False

btn_start.on_click(on_button_click)

# --- จัดหน้าจอแสดงผล ---
ui = widgets.VBox([
    header,
    name_input,
    time_input,
    subject_input,
    widgets.HTML("<br>"), # เว้นบรรทัด
    btn_start,
    output_area
])

display(ui)
