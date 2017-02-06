# esolangs
Interpreters for esoteric programming languages

Currently added:
  * Brainfuck
  * Eitherfuck
  
Eitherfuck was an anonymously proposed Brainfuck derivative, which operates bidirectionally from a central '0' point of the code, with each symbol on the left representing the opposite of its actual function. 

Hello World for example, would be:
```
#<-,+++++++,-,,------->,-,-,-----,-[>>--------<---<-----0+++++[+++++++++>+><<->+>.+++.++>+<++++++++>++---.---->..
```

eitherfuck/converter.py contains a converter from Brainfuck to Eitherfuck.

eitherfuck/musicode.py reads an Eitherfuck code file and plays it as musical notes, with the eight instructions mapping to eight musical notes (C1 - C2). The audio files were obtained from https://github.com/pffy/wav-piano-sound.
