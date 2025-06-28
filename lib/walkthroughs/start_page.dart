import 'package:flutter/material.dart';
import 'package:tutorial_coach_mark/tutorial_coach_mark.dart';

import '/components/start_page_walk_through_tip_widget.dart';
import '/components/walk_through_tip_widget.dart';
import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';

// Focus widget keys for this walkthrough
final textT7dz12v2 = GlobalKey();
final textGpqyupqg = GlobalKey();
final buttonOxubgz3z = GlobalKey();
final buttonI6u55486 = GlobalKey();

/// Start page
///
///
List<TargetFocus> createWalkthroughTargets(BuildContext context) => [
      /// Step 1
      TargetFocus(
        keyTarget: textT7dz12v2,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.top,
            builder: (context, __) => StartPageWalkThroughTipWidget(
              label1: 'Project Title: ',
              explanation1: 'ReVibe     ',
              label2: 'Name: ',
              explanation2: 'Ina     ',
              label3: 'GitHub and edX Usernames: ',
              explanation3: 'Banina94     ',
              label4: 'Location: ',
              explanation4: 'NY, USA     ',
              label5: 'Date Recorded: ',
              explanation5: '12/09/2024     ',
              label6: 'Tool:',
              explanation6: 'Flutterflow AI',
            ),
          ),
        ],
      ),

      /// Step 2
      TargetFocus(
        keyTarget: textGpqyupqg,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.top,
            builder: (context, __) => WalkThroughTipWidget(
              explanation:
                  'Page loads automatically upon start of application. Navigation available for account creation and account log in.',
            ),
          ),
        ],
      ),

      /// Step 3
      TargetFocus(
        keyTarget: buttonOxubgz3z,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.top,
            builder: (context, __) => WalkThroughTipWidget(
              explanation: 'Navigation for new users to account creation.',
            ),
          ),
        ],
      ),

      /// Step 4
      TargetFocus(
        keyTarget: buttonI6u55486,
        enableOverlayTab: true,
        alignSkip: Alignment.bottomRight,
        shape: ShapeLightFocus.RRect,
        color: Colors.black,
        contents: [
          TargetContent(
            align: ContentAlign.top,
            builder: (context, __) => WalkThroughTipWidget(
              explanation: 'Navigation to log into existing account.',
            ),
          ),
        ],
      ),
    ];
