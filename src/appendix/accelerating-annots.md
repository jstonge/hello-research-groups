# Accelerating annotations

There is this new trend in AI that is called data-driven AI. Basically, it is the idea that quality of annotations is more important for AI systems than smart modeling innovation. Back in my days, we were simply saying garbage in garbage out. But now this is at the multiple level in the training pipeline, but during pre-training and fine-tuning.

## Pre-annotations

You run a model, then use that as basis to annotate.

## Active learning

Not all annotations are equally informative. Seeing the same category over and over again can hurt models' ability to generalize, especially with unbalanced dataset. The idea of active learning is to find the next annotation point that will be the most informative for your model. This can be done in batch easily, or online using something like label studio.