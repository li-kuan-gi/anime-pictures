# anime-pictures

The folder structure is as following:

**work-folder / character-folder / phase-folder / img-file**

where **phase-folder** is either 'train' or 'test'.

One can upload a **work-folder** of the following structure:

**character-folder / img-file**

and then use

`python split_train_test.py --root=work-folder`