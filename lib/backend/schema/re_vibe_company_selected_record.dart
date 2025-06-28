import 'dart:async';

import 'package:collection/collection.dart';

import '/backend/schema/util/firestore_util.dart';
import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class ReVibeCompanySelectedRecord extends FirestoreRecord {
  ReVibeCompanySelectedRecord._(
    DocumentReference reference,
    Map<String, dynamic> data,
  ) : super(reference, data) {
    _initializeFields();
  }

  // "reVibeCompanyName" field.
  String? _reVibeCompanyName;
  String get reVibeCompanyName => _reVibeCompanyName ?? '';
  bool hasReVibeCompanyName() => _reVibeCompanyName != null;

  // "reVibeType" field.
  String? _reVibeType;
  String get reVibeType => _reVibeType ?? '';
  bool hasReVibeType() => _reVibeType != null;

  // "reVibeCompanyDescription" field.
  String? _reVibeCompanyDescription;
  String get reVibeCompanyDescription => _reVibeCompanyDescription ?? '';
  bool hasReVibeCompanyDescription() => _reVibeCompanyDescription != null;

  // "reVibeCompanyPicture" field.
  String? _reVibeCompanyPicture;
  String get reVibeCompanyPicture => _reVibeCompanyPicture ?? '';
  bool hasReVibeCompanyPicture() => _reVibeCompanyPicture != null;

  // "reVibeCompanyPoints" field.
  double? _reVibeCompanyPoints;
  double get reVibeCompanyPoints => _reVibeCompanyPoints ?? 0.0;
  bool hasReVibeCompanyPoints() => _reVibeCompanyPoints != null;

  // "reVibeActionQuantity" field.
  double? _reVibeActionQuantity;
  double get reVibeActionQuantity => _reVibeActionQuantity ?? 0.0;
  bool hasReVibeActionQuantity() => _reVibeActionQuantity != null;

  void _initializeFields() {
    _reVibeCompanyName = snapshotData['reVibeCompanyName'] as String?;
    _reVibeType = snapshotData['reVibeType'] as String?;
    _reVibeCompanyDescription =
        snapshotData['reVibeCompanyDescription'] as String?;
    _reVibeCompanyPicture = snapshotData['reVibeCompanyPicture'] as String?;
    _reVibeCompanyPoints =
        castToType<double>(snapshotData['reVibeCompanyPoints']);
    _reVibeActionQuantity =
        castToType<double>(snapshotData['reVibeActionQuantity']);
  }

  static CollectionReference get collection =>
      FirebaseFirestore.instance.collection('reVibeCompanySelected');

  static Stream<ReVibeCompanySelectedRecord> getDocument(
          DocumentReference ref) =>
      ref.snapshots().map((s) => ReVibeCompanySelectedRecord.fromSnapshot(s));

  static Future<ReVibeCompanySelectedRecord> getDocumentOnce(
          DocumentReference ref) =>
      ref.get().then((s) => ReVibeCompanySelectedRecord.fromSnapshot(s));

  static ReVibeCompanySelectedRecord fromSnapshot(DocumentSnapshot snapshot) =>
      ReVibeCompanySelectedRecord._(
        snapshot.reference,
        mapFromFirestore(snapshot.data() as Map<String, dynamic>),
      );

  static ReVibeCompanySelectedRecord getDocumentFromData(
    Map<String, dynamic> data,
    DocumentReference reference,
  ) =>
      ReVibeCompanySelectedRecord._(reference, mapFromFirestore(data));

  @override
  String toString() =>
      'ReVibeCompanySelectedRecord(reference: ${reference.path}, data: $snapshotData)';

  @override
  int get hashCode => reference.path.hashCode;

  @override
  bool operator ==(other) =>
      other is ReVibeCompanySelectedRecord &&
      reference.path.hashCode == other.reference.path.hashCode;
}

Map<String, dynamic> createReVibeCompanySelectedRecordData({
  String? reVibeCompanyName,
  String? reVibeType,
  String? reVibeCompanyDescription,
  String? reVibeCompanyPicture,
  double? reVibeCompanyPoints,
  double? reVibeActionQuantity,
}) {
  final firestoreData = mapToFirestore(
    <String, dynamic>{
      'reVibeCompanyName': reVibeCompanyName,
      'reVibeType': reVibeType,
      'reVibeCompanyDescription': reVibeCompanyDescription,
      'reVibeCompanyPicture': reVibeCompanyPicture,
      'reVibeCompanyPoints': reVibeCompanyPoints,
      'reVibeActionQuantity': reVibeActionQuantity,
    }.withoutNulls,
  );

  return firestoreData;
}

class ReVibeCompanySelectedRecordDocumentEquality
    implements Equality<ReVibeCompanySelectedRecord> {
  const ReVibeCompanySelectedRecordDocumentEquality();

  @override
  bool equals(
      ReVibeCompanySelectedRecord? e1, ReVibeCompanySelectedRecord? e2) {
    return e1?.reVibeCompanyName == e2?.reVibeCompanyName &&
        e1?.reVibeType == e2?.reVibeType &&
        e1?.reVibeCompanyDescription == e2?.reVibeCompanyDescription &&
        e1?.reVibeCompanyPicture == e2?.reVibeCompanyPicture &&
        e1?.reVibeCompanyPoints == e2?.reVibeCompanyPoints &&
        e1?.reVibeActionQuantity == e2?.reVibeActionQuantity;
  }

  @override
  int hash(ReVibeCompanySelectedRecord? e) => const ListEquality().hash([
        e?.reVibeCompanyName,
        e?.reVibeType,
        e?.reVibeCompanyDescription,
        e?.reVibeCompanyPicture,
        e?.reVibeCompanyPoints,
        e?.reVibeActionQuantity
      ]);

  @override
  bool isValidKey(Object? o) => o is ReVibeCompanySelectedRecord;
}
