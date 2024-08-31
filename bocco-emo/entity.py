# クラスの型定義しています（変更しないで）
import pprint
from typing import List, Union

from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class PrintModel(BaseModel):
    def __str__(self):
        return pprint.pformat(self.dict())


@dataclass
class Webhook:
    # Webhookの送信先のURL
    url: str

    # 現在設定されているWebhookの情報
    description: str = ""


# 現在設定されているWebhookの情報
class WebhookInfo(PrintModel):
    # Webhookの設定に関する説明書き
    description: str

    # Webhookを受け取る対象のイベントの一覧
    events: List[str]

    # Webhookの設定状態
    status: str

    # WebhookリクエストのHTTP Headerに含まれるX-Platform-API-Secretと同一の文字列。
    secret: str

    # Webhookの送信先のURL
    url: str


# 部屋に参加しているメンバーの情報
class EmoRoomMember(PrintModel):
    # メンバーのid
    uuid: str

    # メンバーの種別
    user_type: str

    # メンバーのニックネーム
    nickname: str

    # メンバーのプロフィール画像のURL
    profile_image: str


# 部屋に投稿されたテキストメッセージの内容
class EmoMessage(PrintModel):

    ja: str


# 部屋に投稿されたメッセージの情報
class EmoMessageInfo(PrintModel):
    # メッセージの順序関係を示すシーケンス値
    sequence: int

    # メッセージのid
    unique_id: str

    # メッセージを投稿したメンバーの情報
    user: EmoRoomMember

    # テキストメッセージの内容
    message: EmoMessage

    # メッセージのタイプ
    media: str

    # 送信された音声ファイルのURL
    audio_url: str

    # 送信された画像ファイルのURL
    image_url: str

    # メッセージの言語
    lang: str


# Webhookで受信した新規メッセージ受信イベントに関する情報
class EmoWebhookMessage(PrintModel):
    # BOCCO emoが受信したメッセージを示す値
    message: EmoMessageInfo


# BOCCO emoが発話した内容に関する情報
class EmoTalk(PrintModel):
    # 発話した内容を示すテキスト
    talk: str


# Webhookで受信した発話完了イベントに関する情報
class EmoWebhookEmoTalk(PrintModel):
    # BOCCO emoが発話した内容に関する情報
    emo_talk: EmoTalk


# レーダセンサが検知したイベントの情報
class EmoRadar(PrintModel):
    # BOCCO emoの近くに人がいる時に、true が設定されます。
    begin: bool

    # BOCCO emoの近くから人が立ち去った時に、true が設定されます。
    end: bool

    # BOCCO emoのすぐ近くに人がいる時に、true が設定されます。
    near_begin: bool

    # BOCCO emoのすぐ近くから人が立ち去った時に、true が設定されます。
    near_end: bool


# Webhookで受信した内蔵レーダーセンサイベントに関する情報
class EmoWebhookRadar(PrintModel):
    # レーダセンサが検知したイベントの情報
    radar: EmoRadar


# 受信したWebhookの内容
class WebhookBody(PrintModel):
    # リクエストの同一性を示す、一意の文字列
    request_id: str

    # BOCCO emoを識別する一意なID
    uuid: str

    # BOCCO emoの製造番号
    serial_number: str

    # BOCCO emoに設定されているニックネーム
    nickname: str

    # イベントが発生した時刻を示すUNIX Timestamp
    timestamp: int

    # 発生したイベントの種別を示す文字列
    event: str

    # 発生したイベントの詳細を示すオブジェクト
    data: Union[
        EmoWebhookEmoTalk,
        EmoWebhookMessage,
        EmoWebhookRadar,
        dict,
    ]

    # Webhook受信者を示すid
    receiver: str
