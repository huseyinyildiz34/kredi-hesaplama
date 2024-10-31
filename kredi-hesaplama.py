import gradio as gr

# Bankalar ve vadelerine göre faiz oranları (yıllık bazda yüzde olarak)
banks = {
    "Banka A": {3: 13.2, 6: 13.8, 9: 14.4, 12: 15.6, 24: 16.8, 36: 18.0},
    "Banka B": {3: 14.4, 6: 15.0, 9: 15.6, 12: 16.8, 24: 18.0, 36: 19.2},
    "Banka C": {3: 12.6, 6: 13.2, 9: 13.8, 12: 14.4, 24: 15.6, 36: 16.8},
    "Banka D": {3: 13.8, 6: 14.4, 9: 15.0, 12: 16.2, 24: 17.4, 36: 18.6},
    "Banka E": {3: 15.0, 6: 15.6, 9: 16.2, 12: 17.4, 24: 18.6, 36: 19.8}
}

# Hesaplama fonksiyonu
def calculate_payment(bank, term, loan_amount):
    # Yıllık faiz oranını al ve aylık faiz oranına çevir
    annual_rate = banks[bank][term] / 100
    monthly_rate = annual_rate / 12  # Aylık faiz oranı
    
    # Toplam ödenecek tutar ve aylık ödeme miktarını hesapla
    total_payment = loan_amount * (1 + monthly_rate * term)
    monthly_payment = total_payment / term
    
    return round(monthly_rate * 100, 2), round(total_payment, 2), round(monthly_payment, 2)

# Gradio arayüzü
demo = gr.Interface(
    fn=calculate_payment,
    inputs=[
        gr.Dropdown(list(banks.keys()), label="Banka Seçin"),
        gr.Dropdown([3, 6, 9, 12, 24, 36], label="Kredi Vadesi (Ay)"),
        gr.Number(label="Kredi Miktarı")
    ],
    outputs=[
        gr.Number(label="Aylık Faiz Oranı (%)"),
        gr.Number(label="Toplam Ödenecek Tutar"),
        gr.Number(label="Aylık Taksit")
    ],
    title="Kredi Faiz Hesaplama Uygulaması",
    description="Bir banka seçin, kredi vadesini ve miktarını girin. Program size faiz oranını, toplam ödenecek tutarı ve aylık taksiti gösterir."
)

# Uygulamayı başlat
demo.launch()
