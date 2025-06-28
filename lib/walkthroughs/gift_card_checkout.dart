import 'package:flutter/material.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';

import '/components/walk_through_tip_widget.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';

// Focus widget keys for this walkthrough
final containerTfqbxzaq = GlobalKey();
final containerQqtq13cr = GlobalKey();

/// Gift Card Checkout
///
///
List<TargetFocus> createWalkthroughTargets(BuildContext context) => [
      /// Step 1
      TargetFocus(
        keyTarget: containerTfqbxzaq,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.bottom,
            builder: (context, __) => WalkThroughTipWidget(
              explanation: 'Gift card reward company selection.',
            ),
          ),
        ],
      ),

      /// Step 2
      TargetFocus(
        keyTarget: containerQqtq13cr,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.top,
            builder: (context, __) => WalkThroughTipWidget(
              explanation:
                  'Order summary containing points used for gift card rewards.',
            ),
          ),
        ],
      ),
    ];
