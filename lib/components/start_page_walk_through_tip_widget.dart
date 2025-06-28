import '/flutter_flow/flutter_flow_theme.dart';
import '/flutter_flow/flutter_flow_util.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:provider/provider.dart';
import 'start_page_walk_through_tip_model.dart';
export 'start_page_walk_through_tip_model.dart';

class StartPageWalkThroughTipWidget extends StatefulWidget {
  const StartPageWalkThroughTipWidget({
    super.key,
    required this.label1,
    required this.explanation1,
    required this.label2,
    required this.explanation2,
    required this.label3,
    required this.explanation3,
    required this.label4,
    required this.explanation4,
    required this.label5,
    required this.explanation5,
    required this.label6,
    required this.explanation6,
  });

  final String? label1;
  final String? explanation1;
  final String? label2;
  final String? explanation2;
  final String? label3;
  final String? explanation3;
  final String? label4;
  final String? explanation4;
  final String? label5;
  final String? explanation5;
  final String? label6;
  final String? explanation6;

  @override
  State<StartPageWalkThroughTipWidget> createState() =>
      _StartPageWalkThroughTipWidgetState();
}

class _StartPageWalkThroughTipWidgetState
    extends State<StartPageWalkThroughTipWidget> {
  late StartPageWalkThroughTipModel _model;

  @override
  void setState(VoidCallback callback) {
    super.setState(callback);
    _model.onUpdate();
  }

  @override
  void initState() {
    super.initState();
    _model = createModel(context, () => StartPageWalkThroughTipModel());
  }

  @override
  void dispose() {
    _model.maybeDispose();

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: FlutterFlowTheme.of(context).secondaryBackground,
      ),
      child: RichText(
        textScaler: MediaQuery.of(context).textScaler,
        text: TextSpan(
          children: [
            TextSpan(
              text: valueOrDefault<String>(
                widget!.label1,
                'label',
              ),
              style: FlutterFlowTheme.of(context).bodyMedium.override(
                    fontFamily: FlutterFlowTheme.of(context).bodyMediumFamily,
                    letterSpacing: 0.0,
                    fontWeight: FontWeight.w800,
                    useGoogleFonts: GoogleFonts.asMap().containsKey(
                        FlutterFlowTheme.of(context).bodyMediumFamily),
                  ),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.explanation1,
                'explanation',
              ),
              style: TextStyle(),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.label2,
                'label2',
              ),
              style: TextStyle(
                fontWeight: FontWeight.w800,
              ),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.explanation2,
                'explanation2',
              ),
              style: TextStyle(),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.label3,
                'label3',
              ),
              style: TextStyle(
                fontWeight: FontWeight.w800,
              ),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.explanation3,
                'explanation3',
              ),
              style: TextStyle(),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.label4,
                'label4',
              ),
              style: TextStyle(
                fontWeight: FontWeight.w800,
              ),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.explanation4,
                'explanation4',
              ),
              style: TextStyle(),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.label5,
                'label5',
              ),
              style: TextStyle(
                fontWeight: FontWeight.w800,
              ),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.explanation5,
                'explanation5',
              ),
              style: TextStyle(),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.label6,
                'label6',
              ),
              style: TextStyle(
                fontWeight: FontWeight.w800,
              ),
            ),
            TextSpan(
              text: valueOrDefault<String>(
                widget!.explanation6,
                'explanation6',
              ),
              style: TextStyle(),
            )
          ],
          style: FlutterFlowTheme.of(context).bodyMedium.override(
                fontFamily: FlutterFlowTheme.of(context).bodyMediumFamily,
                letterSpacing: 0.0,
                useGoogleFonts: GoogleFonts.asMap()
                    .containsKey(FlutterFlowTheme.of(context).bodyMediumFamily),
              ),
        ),
      ),
    );
  }
}
