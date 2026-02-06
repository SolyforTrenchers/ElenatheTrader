#!/usr/bin/env python3
"""
Simple monitoring dashboard for Elena
"""

import asyncio
import os
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


def clear_screen():
    """Clear terminal screen"""
    os.system('clear' if os.name == 'posix' else 'cls')


def print_header():
    """Print dashboard header"""
    print("="*80)
    print("                    ELENA TRADING BOT - LIVE MONITOR")
    print("="*80)
    print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*80)


def print_trader_status(trader_name, status_data):
    """Print status for a single trader"""
    print(f"\n📊 {trader_name}")
    print(f"  Status:    {'🟢 Running' if status_data['running'] else '🔴 Stopped'}")
    print(f"  Trades:    {status_data['trades']}")
    print(f"  Wins:      {status_data['wins']}")
    print(f"  Losses:    {status_data['losses']}")
    print(f"  P&L:       {status_data['pnl_sol']:.4f} SOL")
    if status_data['uptime_seconds']:
        hours = status_data['uptime_seconds'] / 3600
        print(f"  Uptime:    {hours:.1f} hours")


async def monitor():
    """Main monitoring loop"""
    
    # Mock data for now - will be replaced with real data
    traders = {
        "Volume Trader": {
            "running": True,
            "trades": 12,
            "wins": 8,
            "losses": 4,
            "pnl_sol": 2.45,
            "uptime_seconds": 3600
        },
        "Lore Trader": {
            "running": True,
            "trades": 5,
            "wins": 3,
            "losses": 2,
            "pnl_sol": 0.89,
            "uptime_seconds": 3600
        },
        "TikTok Trader": {
            "running": True,
            "trades": 8,
            "wins": 6,
            "losses": 2,
            "pnl_sol": 1.23,
            "uptime_seconds": 3600
        },
        "Copy Trader": {
            "running": True,
            "trades": 15,
            "wins": 11,
            "losses": 4,
            "pnl_sol": 3.67,
            "uptime_seconds": 3600
        }
    }
    
    while True:
        clear_screen()
        print_header()
        
        total_trades = 0
        total_pnl = 0
        
        for trader_name, status in traders.items():
            print_trader_status(trader_name, status)
            total_trades += status['trades']
            total_pnl += status['pnl_sol']
        
        print("\n" + "="*80)
        print(f"TOTAL TRADES: {total_trades} | TOTAL P&L: {total_pnl:.4f} SOL")
        print("="*80)
        print("\n(This is a mock dashboard. Real implementation coming soon!)")
        print("Press Ctrl+C to exit")
        
        await asyncio.sleep(5)


if __name__ == "__main__":
    try:
        asyncio.run(monitor())
    except KeyboardInterrupt:
        print("\n\nMonitoring stopped.")
