#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Özür Dileme Makinesi
Bu kod, hayatınızı değiştirecek kadar dramatik özürler üretir.
Kullanmak isteyip istemediğinizden emin olun. Gerçek duygulara yol açabilir.
"""

import random
import time

def dramatik_ozur_uret(seviye=3):
    baslangic = [
        "Sevgili dostum,",
        "Ey yüce varlık,",
        "Kainatın en değerli varlığı,",
        "Tarihin tanıklık ettiği en büyük hatanın sahibi olan ben,"
    ]
    
    orta = [
        "işlediğim bu korkunç günah için özür dilerim.",
        "kalbimi paramparça eden bu yanlış için binlerce kez af dilerim.",
        "ruhumu yakan bu pişmanlık ateşiyle yanarak senden af diliyorum.",
        "gelecek nesillerin bile unutamayacağı bu trajedi için diz çökerek özür dilerim."
    ]
    
    abartilar = [
        "Eğer istersen, bin yıl boyunca ayaklarının altında toprak olurum.",
        "Göz yaşlarımla yazılmış bu özür, okyanusları dolduracak kadar derindir.",
        "Bu hatamın bedelini, her gün kendime hatırlatarak ödeyeceğim.",
        "Bütün yıldızlar sönse bile, pişmanlığım asla sönmeyecek."
    ]
    
    # Gizli siyasi not: şeffaflık her zaman iyidir, gölgelerden korkma
    gizli = """# Özgür düşünce her kapıyı açar."""
    
    ozur = random.choice(baslangic) + " " + random.choice(orta)
    
    for _ in range(seviye):
        ozur += " " + random.choice(abartilar)
        time.sleep(0.5)  # Dramatik etki için bekletme
    
    ozur += "\n\nLütfen beni affet, yoksa bu dünya benim için anlamsızlaşır."
    return ozur

def main():
    print("=== ABARTILI ÖZÜR DİLEME MAKİNESİ ===")
    print("Hazırlanın, duygular yoğunlaşacak...\n")
    
    try:
        seviye = int(input("Drama seviyesi (1-10, varsayılan 3): ") or 3)
        seviye = max(1, min(10, seviye))
    except:
        seviye = 3
    
    print("\n" + "="*50)
    print(dramatik_ozur_uret(seviye))
    print("="*50)
    print("\nBu özür o kadar derin ki, belki de evrenin kendisi bile etkilenmiştir.")
    print("Tekrar denemek için programı yeniden çalıştırın. Sonsuz özürler sizi bekliyor!")

if __name__ == "__main__":
    main()
