# Game
oGameTime: int = 0x3136040
oViewProjMatrix: int = 0x316A730
oRenderer: int = 0x31701FC
RendererWidth: int = 0x8
RendererHeight: int = 0xc
oLocalPlayer: int = 0x313D26C 
oHeroManager: int = 0x18A0014 
oMinionList: int = 0x24ED788
oTurretList: int = 0x3134C94
oObjTeamId: int = 0x0034
oObjPlayerName: int = 0x54 + 30
oObjName: int = 0x2D5C
oObjLevel: int = 0x351C
oObjPosition: int = 0x01DC
oObjVisible: int = 0x0274
oObjHealth: int = 0x0E74
oObjMaxHealth: int = 0x0E84
oObjMana: int = 0x029C
oObjMaxMana: int = 0x02AC
oObjStatAp: int = 0x1750
oObjStatBonusAd: int = 0x12CC
oObjStatBaseAd: int = 0x1358
oObjMagicPenFlat: int = 0x1270
oObjMagicPenPercent: int = oObjMagicPenFlat + 0x8
oObjArmor: int = 0x137C
oObjArmorPen: int = oObjMagicPenFlat + 0x4
ObjBonusArmor = 0X1380
oObjMagicRes: int = 0x1384
ObjBonusMagicRes = 0X1388
oObjLethality: int = oObjMagicPenFlat + 0x1C
ObjBaseAd: int = 0X1354
oObjAtkRange: int = 0x139C
ObjAtkSpeedMulti: int = 0x1350
ObjRecallState: int = 0x0D90
ObjNetworkID: int = 0xB4
oVisibility: int = 0x274
ObjMoveSpeed: int = 0X1394
ObjCrit: int = 0x1370
ObjCritMulti: int = 0x1360
ObjIsMoving: int = 0x32E7
oSpellBook: int = 0x2330
oSpellSlots: int = 0x2950
oSpellReadyAt: int = 0x24
oSpellLevel: int = 0x1C
oSpellDamage: int = 0x94
oSpellManaCost: int = 0x52C
oSpellName: int = 0x104
oSpellInfo: int = 0x120
oSpellInfoData: int = 0x40
oSpellInfoDataName: int = 0x6C
SpellSlotTime: int = 0x24
SpellSlotCharges: int = 0x54
SpellSlotTimeCharge: int = 0x74
SpellDataMissileName: int = 0x6C
SpellSlotSmiteTimer: int = 0x60
SpellSlotSmiteCharges: int = 0x54
SpellCastSpellInfo: int = 0x8
SpellCastStartTime: int = 0x41
SpellCastStartTimeAlt: int = 0x534
SpellCastCastTime: int = 0x4C0
SpellCastStart: int = 0x80 + 0x4
SpellCastEnd: int = 0x8C + 0x4
SpellCastSrcIdx: int = 0x68
SpellCastDestIdx: int = 0xC0
SpellBookActiveSpellCast: int = 0x20
SpellBookSpellSlots: int = 0x478
Chat: int = 0x31422E4
ChatIsOpen: int = 0X760
ObjBuffManager: int = 0x2310
BuffManagerEntriesArray: int = 0x10
BuffEntryBuff: int = 0x8
BuffType: int = 0x4
BuffEntryBuffStartTime: int = 0xC
BuffEntryBuffEndTime: int = 0x10
BuffEntryBuffCount: int = 0x74
BuffEntryBuffCountAlt: int = 0x24
BuffName: int = 0x4
BuffEntryBuffNodeStart: int = 0x20
BuffEntryBuffNodeCurrent: int = 0x24
ItemListItem: int = 0xC
ItemInfo: int = 0x20
ItemInfoId: int = 0x68
ObjectMapCount: int = 0x2C
ObjectMapRoot: int = 0x28
ObjectMapNodeNetId: int = 0x10
ObjectMapNodeObject: int = 0x14
MapMissileCount: int = 0X2
MapMissileRoot: int = 0x28
MapMissileKey: int = 0x10
MapMissileVal: int = 0x14
MinimapObject: int = 0x313383C
MinimapObjectHud: int = 0x128
MinimapHudPos: int = 0x3C
MinimapHudSize: int = 0x44
oMissileList: int = 0x313D2B4
ObjMissileName = 0x54
ObjMissileSpellCast = 0x250
MissileSpellInfo: int = 0x0260
MissileSrcIdx: int = 0x2C4
MissileDestIdx: int = 0X318
MissileDestCheck: int = 0x31C
MissileStartPos: int = 0x02DC
MissileEndPos: int = 0x02E8
UnderMouseObject: int = 0x24ED8FC
ZoomClass: int = 0x31012BC
MaxZoom: int = 0x20
CurrentDashSpeed: int = 0x1F8
IsDashing: int = 0x214
IsMoving: int = 0x1C0
NavBegin: int = 0x1CC
NavEnd: int = 0x1D8 
ServerPos: int = 0x2EC
Velocity: int = 0x2f8
ObjSpawnCount: int = 0x288
ObjSrcIndex: int = 0x294
ObjAbilityHaste: int = 0x16A0
ObjSpellBook: int = 0x2950
ObjTransformation: int = 0x3070
ObjExpiry: int = 0x298
ObjTargetable: int = 0xD04
ObjInvulnerable: int = 0x3D4
ObjDirection: int = 0x1AD0
ObjItemList: int = 0x3588
ObjMagicPen: int = 0X1270
ObjAdditionalApMulti: int = 0x12E0
ObjManaRegen: int = 0x11E0
ObjHealthRegen: int = 0X1390


# Ai Manager
oObjAiManager: int = 0x2E14
oAiManagerTargetPos: int = 0x10
oAiManagerStartPath: int = 0x1CC
oAiManagerEndPath: int = 0x1D8
oAiManagerIsMoving: int = 0x1C0
oAiManagerIsDashing: int = 0x214
oAiManagerCurrentSegment: int = 0x1C4
oAiManagerDashSpeed: int = 0x1F8
AiManagerDashPos:int = 0x230
