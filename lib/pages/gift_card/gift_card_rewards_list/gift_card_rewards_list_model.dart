import '/backend/backend.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import '/walkthroughs/gift_card_company_list.dart';
import 'dart:ui';
import 'gift_card_rewards_list_widget.dart' show GiftCardRewardsListWidget;
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart'
    show TutorialCoachMark;
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class GiftCardRewardsListModel
    extends FlutterFlowModel<GiftCardRewardsListWidget> {
  ///  State fields for stateful widgets in this page.

  TutorialCoachMark? giftCardCompanyListController;

  @override
  void initState(BuildContext context) {}

  @override
  void dispose() {
    giftCardCompanyListController?.finish();
  }
}
