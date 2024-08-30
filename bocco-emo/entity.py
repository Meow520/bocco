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
    
    
class WebhookInfo(PrintModel):
    """現在設定されているWebhookの情報"""

    description: str
    """Webhookの設定に関する説明書き
    """

    events: List[str]
    """Webhookを受け取る対象のイベントの一覧
    """

    status: str
    """Webhookの設定状態
    """

    secret: str
    """WebhookリクエストのHTTP Headerに含まれるX-Platform-API-Secretと同一の文字列。

    この文字列とX-Platform-API-Secretの値が同一か確かめることで、第三者からの予期せぬリクエストを防ぐことができます。
    """

    url: str
    """Webhookの送信先のURL
    """

class EmoPerformedBy(PrintModel):
    """録音が実行されたきっかけに関する情報"""

    performed_by: str
    """録音が実行されたきっかけのアクションを示す値

        record_button
            本体の録音ボタンが押された場合の値
        vui_command
            音声コマンドでの録音命令が実施された場合の値
    """
class EmoRoomMember(PrintModel):
    """部屋に参加しているメンバーの情報"""

    uuid: str
    """メンバーのid
    """

    user_type: str
    """メンバーの種別
    """

    nickname: str
    """メンバーのニックネーム
    """

    profile_image: str
    """メンバーのプロフィール画像のURL
    """

class EmoMessage(PrintModel):
    """部屋に投稿されたテキストメッセージの内容"""

    ja: str

class EmoWebhookRecording(PrintModel):
    """Webhookで受信した録音イベントに関する情報"""

    recording: EmoPerformedBy
    """録音が実行されたきっかけに関する情報
    """

class EmoMessageInfo(PrintModel):
    """部屋に投稿されたメッセージの情報"""

    sequence: int
    """メッセージの順序関係を示すシーケンス値

    数字の意味は、`こちらのページ <https://platform-api.bocco.me/dashboard/api-docs#get-/v1/rooms/-room_uuid-/messages>`_ をご覧ください。
    """

    unique_id: str
    """メッセージのid
    """

    user: EmoRoomMember
    """メッセージを投稿したメンバーの情報
    """

    message: EmoMessage
    """テキストメッセージの内容
    """

    media: str
    """メッセージのタイプ

    Note
    ----
    text
        テキストメッセージ
    audio
        音声メッセージ
    image
        画像メッセージ
    stamp
        スタンプメッセージ

    """

    audio_url: str
    """送信された音声ファイルのURL
    """

    image_url: str
    """送信された画像ファイルのURL
    """

    lang: str
    """メッセージの言語
    """

class EmoWebhookMessage(PrintModel):
    """Webhookで受信した新規メッセージ受信イベントに関する情報"""

    message: EmoMessageInfo
    """BOCCO emoが受信したメッセージを示す値
    """

class EmoTalk(PrintModel):
    """BOCCO emoが発話した内容に関する情報"""

    talk: str
    """発話した内容を示すテキスト
    """


class EmoWebhookEmoTalk(PrintModel):
    """Webhookで受信した発話完了イベントに関する情報"""

    emo_talk: EmoTalk
    """BOCCO emoが発話した内容に関する情報
    """
    
class WebhookBody(PrintModel):
    """受信したWebhookの内容"""

    request_id: str
    """リクエストの同一性を示す、一意の文字列
    """

    uuid: str
    """BOCCO emoを識別する一意なID
    """

    serial_number: str
    """BOCCO emoの製造番号
    """

    nickname: str
    """BOCCO emoに設定されているニックネーム
    """

    timestamp: int
    """イベントが発生した時刻を示すUNIX Timestamp
    """

    event: str
    """発生したイベントの種別を示す文字列

    Note
    ----
    eventの種類は、`こちらのページ <https://platform-api.bocco.me/dashboard/api-docs#put-/v1/webhook/events>`_ から確認できます。
    """

    data: Union[
        # EmoWebhookTriggerWord,
        EmoWebhookRecording,
        # EmoWebhookVuiCommand,
        # EmoWebhookMotion,
        EmoWebhookEmoTalk,
        # EmoWebhookAccel,
        # EmoWebhookIlluminance,
        # EmoWebhookRadar,
        EmoWebhookMessage,
        # EmoWebhookMovementSensor,
        # EmoWebhookLockSensor,
        # EmoWebhookHumanSensor,
        # EmoWebhookRoomSensor,
        dict,
    ]
    """発生したイベントの詳細を示すオブジェクト

    イベントの種類に応じてデータ構造が変わります。


    Attention
    ----
    eventの種類がfunction_button.pressedの時、dataは空の辞書 {} となります。

    """

    receiver: str
    """Webhook受信者を示すid

        Personal版の場合
            :func:`get_account_info` から確認できるBOCCOアカウントのuuid
        Business版の場合
            法人アカウントでログインした時の `ダッシュボード <https://platform-api.bocco.me/dashboard/>`_
            から確認できる法人向けAPIキーと同じ文字列
    """
