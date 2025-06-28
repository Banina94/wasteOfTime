// Automatic FlutterFlow imports
import '/backend/backend.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'index.dart'; // Imports other custom actions
import '/flutter_flow/custom_functions.dart'; // Imports custom functions
import 'package:flutter/material.dart';
// Begin custom action code
// DO NOT REMOVE OR MODIFY THE CODE ABOVE!

import 'package:firebase_auth/firebase_auth.dart';

Future<bool> changePassword(
    String currentPassword, String currentEmail, String newPassword) async {
  try {
    // Authenticate account
    AuthCredential credential = EmailAuthProvider.credential(
      email: currentEmail,
      password: currentPassword,
    );
    await FirebaseAuth.instance.currentUser!
        .reauthenticateWithCredential(credential);

    // If reauthentication is successful, change the password.
    await FirebaseAuth.instance.currentUser!.updatePassword(newPassword);

    // Password changed successfully.
    return true;
  } catch (e) {
    // Handle reauthentication errors and password change errors.
    return false;
  }
}
// Set your action name, define your arguments and return parameter,
// and then add the boilerplate code using the green button on the right!
