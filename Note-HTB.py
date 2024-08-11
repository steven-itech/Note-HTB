import pyttsx3
import tkinter as tk
import re
import os
from tkinter import messagebox
from fpdf import FPDF

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def tts(message):
    
    engine.say(message)
    engine.runAndWait()

def submit():
    
    subject_entry = subject.get()
    softwares_entry = softwares.get("1.0", tk.END).strip()
    techniques_entry = techniques.get("1.0", tk.END).strip()
    conclusion_entry = conclusion.get("1.0", tk.END).strip()
    pentester_entry = pentester.get()

    softwares_entry = re.sub(r'\.\s+', ". \n", softwares_entry)
    techniques_entry = re.sub(r'\.\s+', ". \n", techniques_entry)
    conclusion_entry = re.sub(r'\.\s+', ". \n", conclusion_entry)
    conclusion_entry = re.sub(r'\.\s+', ". \n", pentester_entry)

    if not all([subject_entry, softwares_entry, techniques_entry, conclusion_entry, pentester_entry]):
        
        warning = "Veuillez remplir l'ensemble des champs, afin de pouvoir créer le rapport !"
        tts(warning)
        
        messagebox.showwarning(title="Note'HTB :", message=warning)
        
        return

    if not all(any(c.isalpha() for c in entry) and any(c.isspace() for c in entry) for entry in [softwares_entry, techniques_entry, conclusion_entry, pentester_entry]):
        
        warning = "Veuillez constituer uniquement votre rapport avec des caractères alphanumériques et des espaces !"
        
        tts(warning)
        messagebox.showwarning(title="Note'HTB :", message=warning)
        
        return

    else:
        
        pdf = FPDF()
        pdf.add_page()

        pdf.add_font("DejaVuSans", "", "DejaVuSans.ttf", uni=True)
        pdf.add_font("DejaVuSans", "B", "DejaVuSans-Bold.ttf", uni=True)

        pdf.set_font("DejaVuSans", size=12)
        pdf.image("hacking.png", x=10, y=10, w=100, h=(246 / 1251) * 100)

        pdf.ln(30)

        pdf.set_font("DejaVuSans", "B", 12)
        pdf.cell(200, 10, txt="RAPPORT :", ln=True, align='C')

        pdf.ln(3)
        pdf.set_font("DejaVuSans", size=12)
        pdf.cell(0, 10, txt=f"Sujet : {subject_entry}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Logiciels utilisés : {softwares_entry}", ln=True, align='L')
        pdf.cell(0, 10, txt=f"Techniques utilisées : {techniques_entry}", ln=True, align='L')

        pdf.ln(3)
        pdf.multi_cell(0, 10, txt=f"Conclusion :\n{conclusion_entry}", align='L')
        
        pdf.cell(0, 10, txt=f"Pentester : {pentester_entry}", ln=True, align='L')

        pdf_name = f"Rapport - {subject_entry}.pdf"
        pdf.output(pdf_name)

        confirmation = f"Le rapport a été créé et enregistré sous le nom de : {pdf_name} !"
        
        tts(confirmation)
        messagebox.showinfo(title="Note'HTB :", message=confirmation)

if __name__ == "__main__":
    
    window = tk.Tk()
    window.title("Note'HTB :")
    window.iconbitmap("htb.ico")
    window.geometry("755x640")
    window.resizable(False, False)

    tk.Label(window, text="Quel est le sujet de votre rapport ?", font=("Arial", 12)).place(x=5, y=10)
    subject = tk.Entry(window, font=("Arial", 12), width=25)
    subject.place(x=10, y=40)

    tk.Label(window, text="Quels sont les logiciels que vous avez utilisés ?", font=("Arial", 12)).place(x=10, y=80)
    softwares = tk.Text(window, font=("Arial", 12), height=10, width=40)
    softwares.place(x=10, y=110)

    tk.Label(window, text="Quelles sont les techniques que vous avez utilisées ?", font=("Arial", 12)).place(x=380, y=80)
    techniques = tk.Text(window, font=("Arial", 12), height=10, width=40)
    techniques.place(x=380, y=110)

    tk.Label(window, text="Quelle est la conclusion ?", font=("Arial", 12)).place(x=10, y=300)
    conclusion = tk.Text(window, font=("Arial", 12), height=10, width=81)
    conclusion.place(x=10, y=330)

    tk.Label(window, text="Quel est le prénom et le nom de famille du pentester ?", font=("Arial", 12)).place(x=10, y=520)
    pentester = tk.Entry(window, font=("Arial", 12), width=41)
    pentester.place(x=10, y=550)

    submit_button = tk.Button(window, text="Soumettre !", font=("Arial", 12), command=submit)
    submit_button.place(x=10, y=590, width=150)
    
    window.mainloop()