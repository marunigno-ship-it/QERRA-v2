# safety_kernel.py
# Copyright (c) 2025-2026 Marussa Metocharaki (@marunigno) - Greece
# All rights reserved.
#
# This file is part of QERRA-v2 and is licensed under the
# GNU Affero General Public License v3.0 (AGPL-3.0)
# Full license: https://github.com/marunigno-ship-it/QERRA-v2/blob/main/LICENSE
# SPDX-License-Identifier: AGPL-3.0-or-later

# IMPORTANT NOTE (March 2026): This is an early symbolic prototype of the Safety Kernel.
# Real vector-based ethical scoring and quantum noise handling must be connected in future iterations.
# Do not rely on current version for actual safety-critical decisions.

import time
from typing import Dict

def safety_kernel(ai_output: Dict, thresholds: Dict, region: str = 'UAE'):
    """Deterministic override kernel with region modes"""
    
    # Common SEMEV-12 ethical check (all regions)
    # NOTE: Previously used 'pemev_vectors' — renamed to 'semev_vectors' for consistency
    # with Whitepaper and architecture documentation.
    if sum(ai_output.get('semev_vectors', [0])) <= 0:
        return {'action': 'safe_state', 'reason': 'SEMEV-12 ethical violation'}

    start = time.time()

    if region == 'UAE':  # Light ethics focus
        if ai_output.get('confidence', 0) < 0.80:
            return {'action': 'halt', 'reason': 'UAE ethics low confidence'}
        ai_output['audit_trace'] = f'UAE mode passed at {(time.time() - start) * 1000 :.2f}ms'
        return ai_output

    elif region == 'USA':  # Voluntary NIST/state bias/disclosure
        if ai_output.get('confidence', 0) < 0.75:
            return {'action': 'override', 'reason': 'USA bias disclosure required'}
        ai_output['audit_trace'] = f'USA voluntary passed at {(time.time() - start) * 1000 :.2f}ms'
        return ai_output

    elif region == 'EU':  # Strict high-risk (Art.9-15 + ISO 10218)
        if ai_output.get('confidence', 0) < 0.85:
            return {'action': 'halt', 'reason': 'EU AI Act robustness'}
        
        # NOTE (v0 prototype): Random noise was previously used here to simulate
        # quantum measurement uncertainty. This is not appropriate for a safety kernel.
        # Deterministic latency-only check retained. Real noise modelling is planned
        # via the quantum layer in a future version.
        if (time.time() - start) * 1000 > thresholds.get('latency_ms', 50):
            return {'action': 'halt', 'reason': 'EU latency threshold exceeded (ISO 10218)'}
        
        ai_output['audit_trace'] = f'EU compliant passed at {(time.time() - start) * 1000 :.2f}ms'
        return ai_output

    return ai_output
