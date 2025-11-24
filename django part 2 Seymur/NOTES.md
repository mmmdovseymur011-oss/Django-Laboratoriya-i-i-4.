

Layihəmi qurub çalışdırdım və əsas hissələri bir-birinə bağladım:
- Django layihəm (`mysite`) və tətbiqim (`main`) hazırdır; app-i qeydiyyata saldım və URL-ləri kök `urls.py`-yə qoşdum.
- `home` görünüşü şablonumu (`main/templates/index.html`) qaytarır; dizaynımı birbaşa bu şablonda yerləşdirib ekranda görürəm.
- Statik fayllar `main/static/style.css` vasitəsilə yüklənir və dev serverdə `static()` marşrutlaması ilə servis olunur.

Öyrəndiklərim:
- Django-da MVT axını: sorğu URL-dən başlayıb view-ə ötürülür, oradan şablon render olunur və cavab kimi qayıdır.
- Yeni tətbiq əlavə edəndə onu `INSTALLED_APPS`-ə yazmaq və `urls.py`-də `include` vasitəsilə marşrutlamaq lazımdır.
- Statik resurslar üçün `static` qovluğundan istifadə etmək və dev mühitində `static()` marşrutunu açmaq CSS-in problem yaratmamasını təmin edir.
- Sadə bir statik səhifəni Django-nun templating sistemi ilə necə ayağa qaldırmaq və öz HTML/CSS dizaynımı ora yerləşdirmək mümkündür.
- MVT vs MVC: Django-da “controller” rolunu URLconf + view birlikdə icra edir; “view” (MVT-dəki “Template”) isə təqdimat qatıdır. MVC-dəki “Model” eynidir, “View” isə Django-da “Template”ə uyğun gəlir. Django-nun inteqrasiya olunmuş URL yönləndiricisi, orta qat və ORM-i bu fərqi praktikada sadələşdirir.
