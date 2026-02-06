#!/usr/bin/env python3
"""
Check wallet balances for all Elena traders
"""

import asyncio
import os
from dotenv import load_dotenv
from solana.rpc.async_api import AsyncClient
from solders.pubkey import Pubkey

load_dotenv()


async def check_balance(client: AsyncClient, wallet_address: str, name: str):
    """Check SOL balance for a wallet"""
    try:
        pubkey = Pubkey.from_string(wallet_address)
        response = await client.get_balance(pubkey)
        balance_lamports = response.value
        balance_sol = balance_lamports / 1_000_000_000
        
        print(f"{name:20} | {wallet_address:44} | {balance_sol:>10.4f} SOL")
        return balance_sol
    except Exception as e:
        print(f"{name:20} | {wallet_address:44} | Error: {e}")
        return 0


async def main():
    """Main function"""
    rpc_url = os.getenv('SOLANA_RPC_URL', 'https://api.mainnet-beta.solana.com')
    client = AsyncClient(rpc_url)
    
    wallets = {
        "Volume Trader": "Dsfm1XdBWBF68aSAYqZoTP6PRzxc4ZGgeXU14Zw8XAGU",
        "Lore Trader": "3zJqfGWg577XLmyNk7XGF8WQvxTWWVghj7diop1FrYeE",
        "TikTok Trader": "AgqPKDQpubJcnahXVeSdQy4KimVuQearp4FKokRASXPu",
        "Copy Trader": "CkSAH87iysawMBVaWginNW1tcWDSJ3x9UuL8Lkfjmmuu",
    }
    
    print("\n" + "="*80)
    print("Elena Wallet Balances")
    print("="*80)
    print(f"{'Trader':20} | {'Wallet Address':44} | {'Balance':>12}")
    print("-"*80)
    
    total = 0
    for name, address in wallets.items():
        balance = await check_balance(client, address, name)
        total += balance
    
    print("-"*80)
    print(f"{'TOTAL':20} | {' ':44} | {total:>10.4f} SOL")
    print("="*80 + "\n")
    
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
