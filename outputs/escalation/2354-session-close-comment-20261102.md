Session 20261101/02 (9ee0965a), Developer Mode, handed over at session close. The researcher's words in this session, verbatim, in order:

1. "#2354 for adding the surface group column."
2. "the description column is completed, but not recorded (you left this out previously) only add the layer column if it is really meaningful. if it has no information that confirms why you made the decision then it is useless, especially of the column is mostly the same.  I would expect the kinds of being would be differentiated by concept-groups, even better if the split at domain level, like you have done with feeling."
3. "Accept"
4. "please confirm that you are aware that both M-code clusters T-code clusters and cluster-subgroups have mixtures of surfaces allocated to them that does not follow the differentiation of concepts where the focus are in inner being behaviour, inner being status, and beings as entitities. It is expected that a large percentage of surface words will be supporting or qualifying of the three groups."
5. "you are going to do a lot of work, gather information from various sources, it is vital that you record your workings and assumptions and not loose it."
6. "proceed"
7. "I am unable to make the open decision verdicts - I did not look at the data to allow me the make the judgement.  D1 looks like you are asking if you should record a marker to show which surface group a supporting or qualifying word support. This is a many to many relationship, and may be very confusing. more importantly it is to capture the use of the word to make it a qualifing word. for example "within" it is describing where something is, and that something can be a behaviuour, but within cannot be used as a behaviour.  D2 - yes, you obviously created M85 recently and that has not gone through sub group processing.  otherwise - it seems you just need to continue."
8. "Yes, add qualifier"
9. "each cluster should have sub groups. This work was done a couple of days/week ago for all other clusters, but it never took place for M85"
10. "I am talking about the new cluster for beings you created"
11. "sounds like I read your comment on sub clusters for M85 wrong. ignore. continue with Draft v4"
12. "Q1 - my take out list is just a small sample, it does not nearly represent an operational take out list. you already proven that the list may not be correct. So ignore the list. I expect all surfaces in the corpus to be considered, nothing is casted away.  Q2 - this question make me think you are getting entangled. what does the qualifyer subgroups in clusters have to do with where concept qualifyer pairs live?  Q3 I have now created a working ollama local host on a server. it will be sensible to make that to work for Q3.  Q4 is the next work package after this is finished."
13. "I would hope you are going to process a surface once, and not process every occurance of the same surface.  verse_lexical have every occurance and loads of duplicates.  I really am thinking you still do not have a handle on this job, by asking me if you should process 102325 pairs?"
14. "q3 above. the next step is to ensure you access the correct ollama server and that the appropriate model is installed."
15. (pasted) `$env:OLLAMA_HOST = 'http://192.168.83.113:11434'` and `& 'C:\Users\lerouxc\AppData\Local\Programs\Ollama\ollama.exe' list`
16. "the server is no longer a local desktop, it is ubuntu server with significantly more resources. advise on which model to use"
17. "can you use ollama on the host to give you the server specifications"
18. "I am loading qwen3 at the moment.  can you work towards setting up the infrastructure for you to access and work with the host."
19. "ip changed to 192.168.83.114 , I do have a ssh, provide a script for me to add it to the environment"
20. "script ran sucessfully. server user "leroux" ,  qwen3:30b is in the process of upload, almost done."
21. "is there an error in your script?" (with the PowerShell output: ssh not recognised in a window opened before the PATH change)
22. "ps now authorised"
23. (pasted) the output of `Start-Service ssh-agent` and `ssh-add`: "Could not open a connection to your authentication agent."
24. "done"
25. "proceed"
26. "there is a fundamental issue.  previously I noticed that the surface of particles and other objects that is used in a multi span is set to the the same surface as the main strong in the multi span. previously this was identified as an error and bad practice.  if this issue permeates in the data you are using then we may be facing a critical scenario of working with wrong data."
27. "Use my approach"
28. "decisions 1: I suggest a qualifyer, the context will resolve who is being referred to, which is only relevant when the verse is read, and not to determine concept membership."
29. "p2 and p3 decisions is not for me to make - you have the instructions use you best judgement."
30. "I also want to make a change to the ollama host server to reconfigure the CPUs and memory.  Also, can you talk me through the results. what does the model produce, and where is it written to? is it written continuious or only at the end? does the build provide for a restart point, or will it all need to be redone if something goes wrong."
31. "I am  working on the server.  Explain : "For one English surface string, I send its Strong's codes with their glosses." what does this mean in practical terms"
32. "no!  this is moving backwards. why are you doing this. why are you not using the list of surfaces and apply the test to it."
33. "what is the purpose of the surface pair"
34. "lets pause.  I need to dig deeper."
35. "I think i need to do a session-close so I can start from a different angle."

What was done (BUILD 443 to 446; the full workings, rulings 1 to 18 and findings 1 to 30 are in `outputs/escalation/2354-working-log.md`, which is the living record):
- `surface_subgroup.surface_group` column and its five values (behaviour, inner_being_state, being, qualifier, not_allocated), BUILD 443 and 444. Nothing writes the column.
- Table `surface_pair_verdict` (empty) and the Ollama settings (module ollama: host 192.168.83.114:11434, model qwen3:30b; module surface_judge), BUILD 445; modules added to enum.config_module. Named snapshot iba-20261102T104709Z-2354-pair-verdict.db.
- Library `iba/app/lib/surfacejudge.py` and pilot script `iba/app/staging/surface_judge_pilot_2354/temp_2354_pilot.py` (BUILD 446): never run on the per-surface design; the pair-based pilot v1 (7 surfaces) was stopped and is kept as the record.
- SSH to the server works with the key ~/.ssh/id_ed25519_iba (authorised by the researcher for user leroux). Server: zeta-assist, 8 cores Xeon E5-2620 v4, 76 GB RAM, no GPU; the researcher is reconfiguring it.

Findings that matter for the restart: (a) multi-code spans: 52.4 percent of verse_lexical rows share the span's English among their codes and particles (H9xxx) keep it by BUILD 428's rule: 34,865 of 101,458 distinct pairs are particle pairs; 1,255 concept pairs occur only in spans with 2+ non-particle codes (finding 28); (b) the pair-based judging did not work (cost, quality; finding 29); (c) the researcher's correction: apply the test to the list of surfaces, one verdict per distinct surface (finding 30, ruling 18).

Open for the researcher: the angle to restart from; whether surface_pair_verdict is replaced by a per-surface table (my lean: yes; the pair has no job in the surface test); whether the multi-code span rule of BUILD 428 and a head marker in verse_lexical are raised as their own escalation. Plan v5 is partly superseded (pair kinds, particle rule, per-pair table); the working log is current. Not done: no verdict loaded, surface_group still NULL, no tool registered (work package, handler, PS front, grants, test plan).
