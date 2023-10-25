import aiohttp
import json
import hmac
import hashlib
import time
import random
import secrets

class liqPay:
    def __init__(self, public_key: str, private_key: str) -> None:
        self.public_key = public_key
        self.private_key = private_key
        self.base_url = "https://www.liqpay.ua/api"
        self.timeout = aiohttp.ClientTimeout(total=360)

    def _signature_headers(self, data):
        jsonStr = json.dumps(data).encode()
        sign = hmac.new(bytes(self.private_key, 'UTF-8'), jsonStr, hashlib.sha1).hexdigest()
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-LiqPay-Auth': f"{self.public_key}:{sign}"
        }
        return headers

    async def create_invoice(self, amount: float, success_url: str, comment: str) -> dict:
        url = f"{self.base_url}/3/checkout"
        params = {
            "version": 3,
            "action": "pay",
            "amount": amount,
            "currency": "UAH",
            "description": comment,
            "order_id": f'{time.time()}_{secrets.token_hex(random.randint(5, 10))}',
            "language": "uk",
            "sandbox": 1,
            "result_url": success_url,
            "server_url": success_url,
            "paytypes": "liqpay",
        }
        headers = self._signature_headers(params)
        async with aiohttp.ClientSession(headers=headers, timeout=self.timeout) as session:
            response = await session.post(url=url, headers=headers, json=params)

            res = await response.json()
            await session.close()
            return res

    async def status_invoice(self, invoice_id: str) -> bool:
        url = f"{self.base_url}/3/transaction/status"
        params = {
            "version": 3,
            "action": "status",
            "transaction_id": invoice_id,
        }
        headers = self._signature_headers(params)
        async with aiohttp.ClientSession(headers=headers, timeout=self.timeout) as session:
            response = await session.post(url=url, headers=headers, json=params)
            res = await response.json()
            await session.close()
            if res.get('status') == "success":
                return True
            else:
                return False

    async def get_balance(self):
        url = f"{self.base_url}/3/report/balance"
        params = {
            "version": 3,
        }
        headers = self._signature_headers(params)
        async with aiohttp.ClientSession(headers=headers, timeout=self.timeout) as session:
            response = await session.post(url=url, headers=headers, json=params)
            res = await response.json()
            await session.close()
            if res.get('result') == "ok":
                return res.get('balance')
            else:
                return None


async def refund_invoice(self, invoice_id: str) -> bool:
    url = f"{self.base_url}/3/transaction/refund"
    params = {
        "version": 3,
        "action": "refund",
        "transaction_id": invoice_id,
    }
    headers = self._signature_headers(params)
    async with aiohttp.ClientSession(headers=headers, timeout=self.timeout) as session:
        response = await session.post(url=url, headers=headers, json=params)
        res = await response.json()
        await session.close()
        if res.get('status') == "success":
            return True
        else:
            return False
