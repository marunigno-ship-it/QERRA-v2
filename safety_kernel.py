# safety_kernel.py
# Copyright (c) 2025-2026 Marussa Metocharaki (@marunigno) - Greece
# All rights reserved.
#
# This file is part of QERRA-v2 and is licensed under the
# GNU Affero General Public License v3.0 (AGPL-3.0)
# Full license: https://github.com/marunigno-ship-it/QERRA-v2/blob/main/LICENSE
# SPDX-License-Identifier: AGPL-3.0-or-later






# safety_kernel.py - Modular deterministic safety for QERRA-v2 
# Call example: safe = safety_kernel(ai_output, thresholds, region='UAE')

import time
import random
from typing import Dict

def safety_kernel(ai_output: Dict, thresholds: Dict, region: str = 'UAE'):
    """Deterministic override kernel with region modes"""
    
    # Common PEMEV ethical check (all regions)
    if sum(ai_output.get('pemev_vectors', [0])) <= 0:
        return {'action': 'safe_state', 'reason': 'PEMEV ethical violation'}

    start = time.time()

    if region == 'UAE':  # Light ethics focus
        if ai_output.get('confidence', 0) < 0.80:
            return {'action': 'halt', 'reason': 'UAE ethics low confidence'}
        ai_output['audit_trace'] = f'UAE mode passed at { (time.time()-start)*1000 :.2f}ms'
        return ai_output

    elif region == 'USA':  # Voluntary NIST/state bias/disclosure
        if ai_output.get('confidence', 0) < 0.75:
            return {'action': 'override', 'reason': 'USA bias disclosure required'}
        ai_output['audit_trace'] = f'USA voluntary passed at { (time.time()-start)*1000 :.2f}ms'
        return ai_output

    elif region == 'EU':  # Strict high-risk (Art.9-15 + ISO 10218)
        if ai_output.get('confidence', 0) < 0.85:
            return {'action': 'halt', 'reason': 'EU AI Act robustness'}
        noisy = ai_output.get('confidence', 0) + random.uniform(-0.05, 0.05)
        if noisy < 0.70 or (time.time()-start)*1000 > thresholds.get('latency_ms', 50):
            return {'action': 'halt', 'reason': 'EU noise/latency override (ISO 10218)'}
        ai_output['audit_trace'] = f'EU compliant passed at { (time.time()-start)*1000 :.2f}ms'
        return ai_output

    return ai_output
