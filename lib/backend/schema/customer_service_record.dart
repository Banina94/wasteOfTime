import 'dart:async';

import 'package:collection/collection.dart';

import '/backend/schema/util/firestore_util.dart';
import '/backend/schema/util/schema_util.dart';

import 'index.dart';
import '/flutter_flow/flutter_flow_util.dart';

class CustomerServiceRecord extends FirestoreRecord {
  CustomerServiceRecord._(
    DocumentReference reference,
    Map<String, dynamic> data,
  ) : super(reference, data) {
    _initializeFields();
  }

  // "bugReport" field.
  String? _bugReport;
  String get bugReport => _bugReport ?? '';
  bool hasBugReport() => _bugReport != null;

  // "featureReport" field.
  String? _featureReport;
  String get featureReport => _featureReport ?? '';
  bool hasFeatureReport() => _featureReport != null;

  void _initializeFields() {
    _bugReport = snapshotData['bugReport'] as String?;
    _featureReport = snapshotData['featureReport'] as String?;
  }

  static CollectionReference get collection =>
      FirebaseFirestore.instance.collection('customerService');

  static Stream<CustomerServiceRecord> getDocument(DocumentReference ref) =>
      ref.snapshots().map((s) => CustomerServiceRecord.fromSnapshot(s));

  static Future<CustomerServiceRecord> getDocumentOnce(DocumentReference ref) =>
      ref.get().then((s) => CustomerServiceRecord.fromSnapshot(s));

  static CustomerServiceRecord fromSnapshot(DocumentSnapshot snapshot) =>
      CustomerServiceRecord._(
        snapshot.reference,
        mapFromFirestore(snapshot.data() as Map<String, dynamic>),
      );

  static CustomerServiceRecord getDocumentFromData(
    Map<String, dynamic> data,
    DocumentReference reference,
  ) =>
      CustomerServiceRecord._(reference, mapFromFirestore(data));

  @override
  String toString() =>
      'CustomerServiceRecord(reference: ${reference.path}, data: $snapshotData)';

  @override
  int get hashCode => reference.path.hashCode;

  @override
  bool operator ==(other) =>
      other is CustomerServiceRecord &&
      reference.path.hashCode == other.reference.path.hashCode;
}

Map<String, dynamic> createCustomerServiceRecordData({
  String? bugReport,
  String? featureReport,
}) {
  final firestoreData = mapToFirestore(
    <String, dynamic>{
      'bugReport': bugReport,
      'featureReport': featureReport,
    }.withoutNulls,
  );

  return firestoreData;
}

class CustomerServiceRecordDocumentEquality
    implements Equality<CustomerServiceRecord> {
  const CustomerServiceRecordDocumentEquality();

  @override
  bool equals(CustomerServiceRecord? e1, CustomerServiceRecord? e2) {
    return e1?.bugReport == e2?.bugReport &&
        e1?.featureReport == e2?.featureReport;
  }

  @override
  int hash(CustomerServiceRecord? e) =>
      const ListEquality().hash([e?.bugReport, e?.featureReport]);

  @override
  bool isValidKey(Object? o) => o is CustomerServiceRecord;
}
