---
layout: single
title: "A Case for AI-ready Materials Representation from Experiments"
date: 2026-05-02 10:00:00
author_profile: true
tags:
  - materials
  - representation
  - sim-to-real
  - scattering
  - xrd
  - machine-learning
categories:
  - Blog
excerpt: "We favor computational representations of materials over experimental signals like scattering and spectroscopy, widening the sim-to-real gap."
---

I’ve been sitting on this blog post for a while, but a long-overdue visit to India and a recent career shift have finally given me the headspace to put these thoughts onto paper. In the world of AI for materials science, material representation is the secret sauce. Whether an algorithm succeeds or fails often depends entirely on how we "describe" a material to the machine. Through my recent interviews and interactions with industry leaders, one thing has become clear: everyone agrees that better representations are the key to closing the "sim-to-real" gap—the frustrating distance between a computer’s prediction and what actually happens in a laboratory.

But here is the catch: we are mostly thinking about materials as computer constructs, not physical ones.


Most researchers focus on representing materials as molecular graphs, SMILES strings, or atomic environments. It makes sense; these formats are easy to feed into algorithms designed for images, text, or social networks.

However, what frustrates me is that we have a massive suite of techniques to "visualize" materials in the real world—diffraction, spectroscopy, scattering, and fluorescence—that are being largely ignored as primary AI representations. While micrographs and tomography are popular, they aren't yet reliable for the high-throughput demands of massive discovery campaigns.

When I look at the literature, I see a "shiny object" problem. Many researchers take the latest high-profile algorithm from NeurIPS, apply it to a micrograph dataset, and call it progress—often without a clear description of the actual materials problem they are trying to solve. With the rise of complex AI agents, this space is becoming even more siloed and difficult to navigate.


Building models that truly understand experimental data isn't "sexy" in the traditional ML sense. It’s mathematically grueling. Take the recent controversy over the A-lab paper and its use of automated XRD labeling—it is an incredibly difficult, almost ill-posed problem.

In my work with scattering patterns of nanoscale soft matter, I’ve seen these challenges firsthand. To identify a structure, we look at peak positions, shapes, and patterns (peak ratios). But there is a fundamental issue: redundancy.

Experimental data is filled with redundant information that standard ML algorithms find "unfriendly". Phenomena like "preferential orientation" in XRD can cause missing peaks. In scattering, peaks can span multiple length scales and effectively cancel each other out in the aggregated signal.

This makes it nearly impossible to create the "AlphaFold of Materials" by simply throwing terabytes of data at the problem. In fact, we’re so far from a solution that even human experts often can’t agree on how to describe the same scattering pattern (as seen in the SasFit round-robin study).

I don’t claim to have the silver bullet. But I do know that the current "fashionable" focus on computational-only representation is a mistake.

If you are in a position to guide the next generation of autonomous discovery technology, I urge you to make experimental representation a priority. It is a problem that requires serious resources and dedicated personnel.

Is it a good PhD thesis topic? Absolutely. Will it make you more employable? I’m honestly not sure. The industry leaders currently driving the "Self-Driving Lab" revolution seem more interested in closing the loop using simple peak positions—solving problems they already know how to solve without AI.

To me, that is the biggest pity. We are building the future of science, but we’re still hesitant to tackle its most fundamental challenge: accurately representing the physical world.


recommended_reading:
  - _posts/2026-06-01-gps_functions_boxes.md
  - _posts/2026-07-01-manifold_bandwagon.md

{% include recommended-reading.html %}