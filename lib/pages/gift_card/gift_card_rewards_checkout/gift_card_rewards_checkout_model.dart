import '/components/user_points_widget.dart';
import '/flutter_flow/flutter_flow_icon_button.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import '/flutter_flow/flutter_flow_widgets.dart';
import '/walkthroughs/gift_card_checkout.dart';
import 'dart:ui';
import '/flutter_flow/custom_functions.dart' as functions;
import 'gift_card_rewards_checkout_widget.dart'
    show GiftCardRewardsCheckoutWidget;
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart'
    show TutorialCoachMark;
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';

class GiftCardRewardsCheckoutModel
    extends FlutterFlowModel<GiftCardRewardsCheckoutWidget> {
  ///  State fields for stateful widgets in this page.

  TutorialCoachMark? giftCardCheckoutController;
  // Model for userPoints component.
  late UserPointsModel userPointsModel;

  @override
  void initState(BuildContext context) {
    userPointsModel = createModel(context, () => UserPointsModel());
  }

  @override
  void dispose() {
    giftCardCheckoutController?.finish();
    userPointsModel.dispose();
  }
}
