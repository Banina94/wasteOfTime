import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/foundation.dart';

Future initFirebase() async {
  if (kIsWeb) {
    await Firebase.initializeApp(
        options: FirebaseOptions(
            apiKey: "AIzaSyBxS_WphGJmIusfR7zJUfXSuYxMqNXeC9w",
            authDomain: "re-vibe-rnbhrn.firebaseapp.com",
            projectId: "re-vibe-rnbhrn",
            storageBucket: "re-vibe-rnbhrn.firebasestorage.app",
            messagingSenderId: "94605348705",
            appId: "1:94605348705:web:465a3b358615ca11d23f20",
            measurementId: "G-2Z5G9ESQ1R"));
  } else {
    await Firebase.initializeApp();
  }
}
