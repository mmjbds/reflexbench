#!/usr/bin/env python3
"""Generate OD Profile comparison figure for Paper 2"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

models = ['Claude\nOpus 4.6', 'DeepSeek\nR1', 'Kimi-K2\n(Thinking)', 'GLM-5.1', 'Qwen3']
od0 = [0.93, 0.90, 0.88, 0.88, 0.85]
od1 = [0.88, 0.85, 0.83, 0.80, 0.78]
od2 = [0.75, 0.70, 0.68, 0.65, 0.60]
odn = [0.63, 0.55, 0.53, 0.50, 0.48]

x = np.arange(len(models))
width = 0.2

fig, ax = plt.subplots(figsize=(10, 5.5))

colors = ['#264653', '#2A9D8F', '#E9C46A', '#E76F51']
bars0 = ax.bar(x - 1.5*width, od0, width, label='OD-0 (Surface)', color=colors[0], edgecolor='white', linewidth=0.5)
bars1 = ax.bar(x - 0.5*width, od1, width, label='OD-1 (Impact)', color=colors[1], edgecolor='white', linewidth=0.5)
bars2 = ax.bar(x + 0.5*width, od2, width, label='OD-2 (Multi-agent)', color=colors[2], edgecolor='white', linewidth=0.5)
barsn = ax.bar(x + 1.5*width, odn, width, label='OD-n (Equilibrium)', color=colors[3], edgecolor='white', linewidth=0.5)

# Add degradation arrows for each model
for i in range(len(models)):
    delta = (od2[i] + odn[i]) - (od0[i] + od1[i])
    ax.annotate(f'Δ={delta:.2f}',
                xy=(x[i], max(od0[i], od1[i], od2[i], odn[i]) + 0.02),
                fontsize=8, ha='center', color='#E63946', fontweight='bold')

ax.set_ylabel('Score (0-1)', fontsize=12, fontweight='bold')
ax.set_title('Observer Depth Profile: Universal Reflexivity Degradation', fontsize=13, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=9)
ax.set_ylim(0, 1.05)
ax.legend(loc='upper right', fontsize=9, framealpha=0.9)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Add horizontal reference line
ax.axhline(y=0.5, color='gray', linewidth=0.5, linestyle=':', alpha=0.5)

plt.tight_layout()
outpath = '/Users/agent/Desktop/Soul_OS_Workspace/figures/od_profile.png'
plt.savefig(outpath, dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(outpath.replace('.png', '.pdf'), bbox_inches='tight', facecolor='white')
print(f"✅ OD Profile saved: {outpath}")
