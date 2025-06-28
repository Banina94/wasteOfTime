import 'dart:async';

import 'package:collection/collection.dart';

import '/backend/schema/util/firestore_util.dart';
import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class GiftCardsRecord extends FirestoreRecord {
  GiftCardsRecord._(
    DocumentReference reference,
    Map<String, dynamic> data,
  ) : super(reference, data) {
    _initializeFields();
  }

  // "giftCardRewards" field.
  double? _giftCardRewards;
  double get giftCardRewards => _giftCardRewards ?? 0.0;
  bool hasGiftCardRewards() => _giftCardRewards != null;

  // "giftCardPoints" field.
  double? _giftCardPoints;
  double get giftCardPoints => _giftCardPoints ?? 0.0;
  bool hasGiftCardPoints() => _giftCardPoints != null;

  // "giftCardCompanyDescription" field.
  String? _giftCardCompanyDescription;
  String get giftCardCompanyDescription => _giftCardCompanyDescription ?? '';
  bool hasGiftCardCompanyDescription() => _giftCardCompanyDescription != null;

  // "giftCardCompanyName" field.
  String? _giftCardCompanyName;
  String get giftCardCompanyName => _giftCardCompanyName ?? '';
  bool hasGiftCardCompanyName() => _giftCardCompanyName != null;

  // "giftCardPicture" field.
  String? _giftCardPicture;
  String get giftCardPicture => _giftCardPicture ?? '';
  bool hasGiftCardPicture() => _giftCardPicture != null;

  // "giftCardCompanyURL" field.
  String? _giftCardCompanyURL;
  String get giftCardCompanyURL => _giftCardCompanyURL ?? '';
  bool hasGiftCardCompanyURL() => _giftCardCompanyURL != null;

  void _initializeFields() {
    _giftCardRewards = castToType<double>(snapshotData['giftCardRewards']);
    _giftCardPoints = castToType<double>(snapshotData['giftCardPoints']);
    _giftCardCompanyDescription =
        snapshotData['giftCardCompanyDescription'] as String?;
    _giftCardCompanyName = snapshotData['giftCardCompanyName'] as String?;
    _giftCardPicture = snapshotData['giftCardPicture'] as String?;
    _giftCardCompanyURL = snapshotData['giftCardCompanyURL'] as String?;
  }

  static CollectionReference get collection =>
      FirebaseFirestore.instance.collection('giftCards');

  static Stream<GiftCardsRecord> getDocument(DocumentReference ref) =>
      ref.snapshots().map((s) => GiftCardsRecord.fromSnapshot(s));

  static Future<GiftCardsRecord> getDocumentOnce(DocumentReference ref) =>
      ref.get().then((s) => GiftCardsRecord.fromSnapshot(s));

  static GiftCardsRecord fromSnapshot(DocumentSnapshot snapshot) =>
      GiftCardsRecord._(
        snapshot.reference,
        mapFromFirestore(snapshot.data() as Map<String, dynamic>),
      );

  static GiftCardsRecord getDocumentFromData(
    Map<String, dynamic> data,
    DocumentReference reference,
  ) =>
      GiftCardsRecord._(reference, mapFromFirestore(data));

  @override
  String toString() =>
      'GiftCardsRecord(reference: ${reference.path}, data: $snapshotData)';

  @override
  int get hashCode => reference.path.hashCode;

  @override
  bool operator ==(other) =>
      other is GiftCardsRecord &&
      reference.path.hashCode == other.reference.path.hashCode;
}

Map<String, dynamic> createGiftCardsRecordData({
  double? giftCardRewards,
  double? giftCardPoints,
  String? giftCardCompanyDescription,
  String? giftCardCompanyName,
  String? giftCardPicture,
  String? giftCardCompanyURL,
}) {
  final firestoreData = mapToFirestore(
    <String, dynamic>{
      'giftCardRewards': giftCardRewards,
      'giftCardPoints': giftCardPoints,
      'giftCardCompanyDescription': giftCardCompanyDescription,
      'giftCardCompanyName': giftCardCompanyName,
      'giftCardPicture': giftCardPicture,
      'giftCardCompanyURL': giftCardCompanyURL,
    }.withoutNulls,
  );

  return firestoreData;
}

class GiftCardsRecordDocumentEquality implements Equality<GiftCardsRecord> {
  const GiftCardsRecordDocumentEquality();

  @override
  bool equals(GiftCardsRecord? e1, GiftCardsRecord? e2) {
    return e1?.giftCardRewards == e2?.giftCardRewards &&
        e1?.giftCardPoints == e2?.giftCardPoints &&
        e1?.giftCardCompanyDescription == e2?.giftCardCompanyDescription &&
        e1?.giftCardCompanyName == e2?.giftCardCompanyName &&
        e1?.giftCardPicture == e2?.giftCardPicture &&
        e1?.giftCardCompanyURL == e2?.giftCardCompanyURL;
  }

  @override
  int hash(GiftCardsRecord? e) => const ListEquality().hash([
        e?.giftCardRewards,
        e?.giftCardPoints,
        e?.giftCardCompanyDescription,
        e?.giftCardCompanyName,
        e?.giftCardPicture,
        e?.giftCardCompanyURL
      ]);

  @override
  bool isValidKey(Object? o) => o is GiftCardsRecord;
}
