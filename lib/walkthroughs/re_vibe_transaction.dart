import 'package:flutter/material.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';

import '/components/walk_through_tip_widget.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';

// Focus widget keys for this walkthrough
final containerKq01fhzh = GlobalKey();
final container3azshk3y = GlobalKey();

/// ReVibe Transaction
///
///
List<TargetFocus> createWalkthroughTargets(BuildContext context) => [
      /// Step 1
      TargetFocus(
        keyTarget: containerKq01fhzh,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.bottom,
            builder: (context, __) => WalkThroughTipWidget(
              explanation: 'Selection of ReVibe company.',
            ),
          ),
        ],
      ),

      /// Step 2
      TargetFocus(
        keyTarget: container3azshk3y,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.top,
            builder: (context, __) => WalkThroughTipWidget(
              explanation: 'Detail on points earned from ReVibe activity.',
            ),
          ),
        ],
      ),
    ];
