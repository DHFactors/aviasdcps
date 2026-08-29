"""
================================================================================
 FILE: app/core/database.py
 VERSION: 1.0.0
 DATE: 2026-08-29
 PURPOSE: Supabase PostgreSQL Client Connector & Database Utility Gateway.
================================================================================
"""

import os
import logging
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

SUPABASE_URL: str = os.getenv("SUPABASE_URL", "https://juejexyfktqvimnrboek.supabase.co")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")

supabase: Client = None

if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
        logger.info(" Connected successfully to Supabase PostgreSQL")
    except Exception as e:
        logger.warning(f"⚠️ Could not initialize Supabase client: {e}")
else:
    logger.warning("⚠️ SUPABASE_URL or SUPABASE_KEY missing in .env")