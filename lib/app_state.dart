import 'package:flutter/material.dart';
import '/backend/backend.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'flutter_flow/flutter_flow_util.dart';

class FFAppState extends ChangeNotifier {
  static FFAppState _instance = FFAppState._internal();

  factory FFAppState() {
    return _instance;
  }

  FFAppState._internal();

  static void reset() {
    _instance = FFAppState._internal();
  }

  Future initializePersistedState() async {
    prefs = await SharedPreferences.getInstance();
    _safeInit(() {
      _userPoints = prefs.getDouble('ff_userPoints') ?? _userPoints;
    });
    _safeInit(() {
      _giftCardRewards =
          prefs.getDouble('ff_giftCardRewards') ?? _giftCardRewards;
    });
  }

  void update(VoidCallback callback) {
    callback();
    notifyListeners();
  }

  late SharedPreferences prefs;

  double _userPoints = 0.0;
  double get userPoints => _userPoints;
  set userPoints(double value) {
    _userPoints = value;
    prefs.setDouble('ff_userPoints', value);
  }

  double _giftCardRewards = 0.0;
  double get giftCardRewards => _giftCardRewards;
  set giftCardRewards(double value) {
    _giftCardRewards = value;
    prefs.setDouble('ff_giftCardRewards', value);
  }
}

void _safeInit(Function() initializeField) {
  try {
    initializeField();
  } catch (_) {}
}

Future _safeInitAsync(Function() initializeField) async {
  try {
    await initializeField();
  } catch (_) {}
}
