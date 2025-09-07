[app]
title = HelloApp
package.name = helloapp
package.domain = org.example

# קבצי הפרויקט
source.dir = .
source.include_exts = py,kv,ttf
# אם ברצונך לשים את הפונט בתקייה אחרת, הוסף פה include_patterns מתאים
# source.include_patterns = fonts/*.ttf

version = 1.0
orientation = portrait
fullscreen = 0

# תלות מינימלית
requirements = python3,kivy

# אנדרואיד – גרסאות וכלים
android.api = 34
android.minapi = 21
android.build_tools_version = 34.0.0

# תמיכה בשתי ארכיטקטורות עיקריות כדי למנוע "לא תואם לטלפון"
android.archs = arm64-v8a, armeabi-v7a

# קבלת רישיונות ה-SDK אוטומטית
android.accept_sdk_license = True

# בניית ריליס ויצירת APK (לא AAB)
android.release = 1
android.release_artifact = apk
android.bundle = 0

# חתימה: Buildozer יוצר debug keystore אוטומטית ל-APK ריליס/דיבאג כך שאפשר להתקין מיד.
# אם תרצה keystore משלך לעתיד: android.keystore = mykeystore.jks וכו'

[buildozer]
warn_on_root = 0
log_level = 2
