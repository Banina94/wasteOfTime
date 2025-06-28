import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import '/walkthroughs/re_vibe_transaction.dart';
import 'dart:ui';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart'
    show TutorialCoachMark;
import 're_vibe_transaction_checkout_widget.dart'
    show ReVibeTransactionCheckoutWidget;
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class ReVibeTransactionCheckoutModel
    extends FlutterFlowModel<ReVibeTransactionCheckoutWidget> {
  ///  State fields for stateful widgets in this page.

  TutorialCoachMark? reVibeTransactionController;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    reVibeTransactionController?.finish();
  }
}
