#!/usr/bin/env python
import random
from os import walk

nounPath = "../lists/tygh/noun"
verbPath = "../lists/tygh/verb"
adjectivePath = "../lists/tygh/adjective"

nouns = []
verbs = []
adjectives = []


def loadLists(path,listName):
    print "Loading list %s" % listName
    for (dirpath, dirnames, filenames) in walk(path):
        for file in filenames:
            with open(file) as f:
                listName.extend(f.readlines()


loadLists(nounPath,nouns)
loadLists(verbPath,verbs)
loadLists(adjectivePath,adjectives)


nouns = {}
nouns['p'] = ["paba","pace","pacemaker","pacer","pacifier","pacifism","pacifist","pacing","pack","package","packet","packing","pact","pad","padding","paddock","padlock","paean","pagan","paganism","page","pageant","pageantry","paging","pagoda","pail","pain","paint","paintbrush","painter","painting","pair","pajama","pal","palace","palatability","palate","palazzo","pale","paleoexplosion","palette","pall","palladium","pallet","pallor","palm","palsy","pamphlet","pan","pandemic","pane","panel","paneling","panelization","panic","panjandrum","panorama","pansy","pantheist","pantheon","pantomime","pantry","pap","paper","paperback","paperweight","paprika","par","parable","parachute","parade","paradigm","paradise","paradox","paragon","paragraph","paragraphing","paralanguage","parallel","parallelism","paramagnet","parameter","paranoiac","paraoxon","parapet","paraphernalia","paraphrase","parapsychology","parasite","parasol","parcel","parchment","pardon","parenchyma","parent","parentage","parenthood","pariah","parish","parisology","park","parking","parkway","parlance","parliament","parlor","parody","parole","parquet","parsimony","parsley","parson","parsonage","part","partaker","participant","participation","particle","particular","particularity","parting","partisan","partition","partner","partnership","party","passage","passageway","passenger","passerby","passing","passion","passivity","passport","past","paste","pastel","pasteurization","pastime","pastor","pastry","pasture","pat","patch","patchwork","pate","patent","patenting","paternalism","path","pathologist","pathology","patience","patient","patina","patio","patriarch","patriarchy","patrician","patriot","patriotism","patrol","patrolman","patrolmen","patron","patronage","patsy","patter","pattern","paucity","paunch","pause","pavement","pavilion","paw","pawn","pawnshop","pay","paycheck","payday","paymaster","payment","payoff","payroll","peace","peacetime","peach","peacock","peak","peanut","pear","pearl","peasant","peasanthood","pebble","pecan","peck","peculiarity","pedagogue","pedal","peddler","pedestal","pedestrian","pedigree","peer","peg","pegboard","pellagra","peltry","pemmican","pen","penalty","penance","penchant","pencil","pendulum","penetration","penicillin","peninsula","penman","pennant","penny","pension","pensioner","pentagon","penthouse","penury","people","pepper","pepperoni","peptide","percent","percentage","perception","percolator","percussion","perfectability","perfectibility","perfection","perfectionism","performance","performer","perfume","perfumery","perfusion","peril","perilla","perimeter","period","periodical","periodicity","periphery","perjury","permanence","permissibility","permission","permit","peroxide","perpetration","perpetrator","perpetuation","perplexity","persecution","perseverance","persiflage","persistence","persistent","person","persona","personae","personage","personality","personification","personnel","perspective","perspiration","persuading","persuasion","pertinence","perturbation","perusal","pervaporation","pessimism","pest","pet","petition","petitioner","petroleum","petulance","pfennig","phalanx","phantasy","phantom","pharmacist","pharmacy","phase","pheasant","phenomena","phenomenon","phenonenon","phenothiazine","philanthropist","philantrophy","philharmonic","philology","philosopher","philosophy","phloem","phone","phonograph","phonology","phony","phosgene","phosphate","phosphide","phosphor","photo","photocathode","photograph","photographer","photography","photoluminescence","photomicrograph","photomicrography","photorealism","phrase","phrasemaking","phraseology","phrasing","phthalate","phyla","physician","physicist","physiognomy","physiologist","physiology","physiotherapist","physique","pianism","pianist","piano","piazza","pick","pickaxe","picker","picket","picking","pickle","pickoff","pickup","picnic","picture","picturing","pidgin","pie","piece","pier","piety","piezoelectricity","pig","pigen","pigeon","pigeonhole","pigment","pigskin","pike","pile","pilgrim","pilgrimage","pill","pillage","pillar","pillow","pilot","piloting","pimp","pin","pinball","pinch","pine","pineapple","pinhead","pink","pinnacle","pinochle","pinpoint","pint","pinto","pioneer","pip","pipe","pipeline","piping","pique","piracy","pirate","pirouette","pistachio","pistol","piston","pit","pitch","pitcher","pitchfork","pitching","pitfall","pith","pituitary","pity","pivot","pizza","pizzicato","place","placement","placing","plagiarism","plague","plaid","plain","plaintiff","plan","plane","planeload","planer","planet","planetarium","planetoid","plank","planking","planner","planning","plant","plantain","plantation","planter","planting","plaque","plasm","plasma","plaster","plasterer","plastering","plastic","plasticity","plate","plateau","platform","platinum","platoon","platter","play","playback","playboy","player","playground","playing","playmate","playoff","playroom","playtime","playwright","playwriting","plea","pleader","pleading","pleasance","pleasant","pleasure","pledge","plenipotentiary","plenitude","plenty","pleura","plight","plodding","plot","plow","plowing","pluck","plug","plugugly","plum","plumb","plumber","plumbing","plume","plunder","plundering","plunge","pluralism","plush","plywood","pneumonia","poark","pocket","pocketbook","pocketful","podium","poem","poet","poetry","poignancy","point","pointer","poise","poison","poisoning","poker","polarity","polarization","pole","polecat","polemic","police","policeman","policemen","policing","policy","polio","polish","politician","politicking","politico","polity","polka","poll","pollen","pollution","polo","polonaise","polybutene","polyester","polyether","polyethylene","polyisobutylene","polyisocyanate","polymer","polymerization","polynomial","polyphosphate","polypropylene","polystyrene","pomp","poncho","pond","pony","poodle","pool","pop","pope","poplar","poplin","poppy","poppyseed","populace","popularity","population","porcelain","porch","pore","pork","porosity","porridge","port","portal","porter","portfolio","portico","portion","portrait","portraiture","portrayal","pose","poseur","position","positive","positivism","positivist","posse","posseman","possemen","possession","possessive","possessor","possibility","possum","post","postcard","poster","posterity","postgraduate","postman","postmark","postmen","postponement","postscript","posture","pot","potassium","potato","potboiler","potency","potential","potentiality","potentiometer","pothole","potpourri","pottery","pouch","poultice","poultry","pound","pounding","pout","poverty","pow","powder","powderpuff","power","practicability","practicality","practice","practicing","practitioner","pragmatism","prairie","praise","pram","pranha","prank","prayer","preacher","preaching","preamble","precaution","precedence","precedent","preceding","precept","prechlorination","precinct","precipice","precipitate","precipitin","precision","precocity","precondition","predecessor","predicament","predicator","predictability","prediction","predisposition","prednisone","predominance","predomination","preface","preference","preferment","pregnancy","prejudice","preliminary","prelude","premier","premiere","premise","premium","premix","premonition","preoccupation","preordainment","prep","preparation","prepayment","prepolymer","preponderance","preposition","prepublication","preradiation","prerequisite","prerogative","prescription","presence","present","presentation","presenter","preservation","preserve","presidency","president","pressure","prestidigitator","prestige","presumption","presupposition","pretence","pretense","pretext","prevalence","prevention","preview","prevision","prey","price","pricing","prick","pride","priest","primacy","primary","prime","priming","primitive","primitivism","prince","princesse","principal","principle","print","printer","printing","printmaking","priority","prison","prisoner","privacy","private","privet","privilege","privy","prize","pro","probability","probate","probation","probe","probity","problem","procaine","procedure","proceeding","processing","procession","processional","processor","proclamation","procrastination","procreation","procreativity","proctor","procurement","procurer","prod","prodigy","produce","producer","producing","product","production","productivity","profanity","profession","professional","professionalism","professor","professorship","profet","proficiency","profile","profit","profitability","profoundity","profundity","profusion","progandist","progeny","prognostication","prognosticator","program","programing","programmer","programming","progression","progressivism","prohibition","prohibiton","project","projectile","projection","projector","proletariat","proliferation","prolixity","prolongation","prolusion","promazine","promenade","prominence","promise","promoter","promotion","pronoun","pronouncement","proof","prop","propaganda","propagandist","propagation","propeller","property","prophecy","prophet","propionate","proponent","proportion","proportionality","proposal","proposition","proprieter","proprietor","proprietorship","propriety","propulsion","propylthiouracil","proscription","prose","prosecution","prosecutor","prospect","prosperity","prostate","prostitute","prostitution","protagonist","protease","protection","protege","protein","protest","protocol","proton","protoplasm","prototype","protozoa","protrusion","protuberance","provenance","proverb","providence","province","provincialism","provision","proviso","provocation","prow","prowl","proximity","proxy","prudence","prune","psalm","psalmist","pseudonym","pseudophloem","pseudynom","psi","psyche","psychiatrist","psychiatry","psychoanalyst","psychologist","psychology","psychopath","psychopomp","psychotherapy","psyllium","pterygia","pub","puberty","public","publication","publicity","publisher","publishing","puddle","puke","pull","pulley","pulp","pulpit","pulsation","pulse","pump","pumpkin","pun","punch","punchbowl","puncher","punching","punctuality","punctuation","punditry","pungency","punishment","punk","punster","pup","pupil","puppet","puppy","purchase","purchasing","purgation","purgatory","purge","purging","purification","purism","purity","purple","purpose","purse","pursuer","pursuit","purveyor","push","pussy","pussycat","putout","putt","putter","putty","puzzle","puzzlement","puzzler","pynte","pyorrhea","pyramid","pyre","pyrometer","pyrophosphate","pyschiatrist","python"]

verbs = {}
verbs['p'] = ["pace","paced","pacifies","pacify","pacing","pack","package","packaged","packaging","packed","packing","pad","padded","padding","paddle","padlocked","page","paginated","paid","paide","paie","pained","paint","painted","painting","paints","paired","paled","paling","pall","palletized","palmed","pamper","pampered","pan","paneled","panelized","panic","panicked","panted","panting","pantomimed","paper","parade","paraded","parades","parading","parallel","paralleled","paralleling","parallels","paralyze","paralyzed","paralyzes","paraphrasing","parboiled","parceled","parched","pardon","pardoned","pare","park","parked","parking","parlayed","parley","parodied","parried","parroting","part","partake","partakes","partaking","parted","participate","participated","participates","participating","parting","partnered","partook","party","pass","passed","passes","passing","paste","pasted","pasting","pat","patched","patented","patrol","patrolled","patrolling","patronize","patronized","patronizing","patted","pattered","pattern","patterned","patting","pause","paused","pauses","pausing","pave","paved","paving","paw","pawing","pay","paying","pays","peck","pecked","pedal","peddle","peddled","peed","peeked","peeking","peel","peeled","peeling","peels","peeping","peer","peered","peering","peers","pegged","pegging","pelting","pen","penalized","penciled","penetrate","penetrated","penetrating","penned","people","peopled","peppered","pepping","peptizing","perceive","perceived","perceives","perceiving","perch","perched","perfected","perfecting","perforated","perform","performed","performing","performs","perfumed","perish","perished","perishes","perishing","perk","permeate","permeated","permeates","permit","permits","permitted","permitting","perpetrated","perpetuate","perpetuated","perpetuating","perplex","perplexed","persecuted","perseveres","persist","persisted","persisting","persists","personalized","personified","personifies","personifying","perspired","perspiring","persuade","persuaded","persuading","pertain","pertained","pertaining","pertains","perturbed","perusing","pervaded","pervades","pervading","perverted","pester","pestering","petered","petition","petitioned","petitions","petrified","petted","petting","pfffted","philosophized","philosophizing","phone","phoned","phones","photograph","photographed","photographing","photographs","phrase","phrased","phrasing","pick","picked","picketed","picketing","picking","pickled","picks","picnicked","picture","pictured","pictures","picturing","piddling","piece","pierced","piercing","pile","piled","piles","pilfering","piling","pillage","pillaged","pillared","pilloried","pilot","piloting","pin","pinch","pinched","pinching","pinging","pinioned","pinned","pinning","pinpoint","pinpointing","pioneer","pioneered","pioneering","piped","piping","piss","pit","pitch","pitched","pitching","pitied","pity","pivoting","placating","place","placed","places","placing","plague","plagued","plan","plane","planed","plank","planned","planning","plans","plant","planted","planting","plastered","plated","platted","play","played","playing","plays","plead","pleaded","pleading","pleads","please","pleased","pleases","pleasure","pledged","plied","plinking","plod","plodded","plodding","plopped","plot","plots","plotted","plotting","plow","plowed","plowing","pluck","plucked","plucking","plug","plugged","plugging","plumbed","plumed","plummeting","plumped","plunder","plunge","plunged","plunges","plunging","plunking","poach","poaches","pocketed","poetizing","point","pointed","pointing","points","poised","poison","poisoned","poisoning","poke","poked","pokes","poking","polarize","polarized","polarizing","policed","policing","poling","polish","polished","polishing","polled","polling","polluted","pomaded","ponder","pondered","pondering","pontificates","pooched","pool","pooled","pooling","pop","popped","popping","pops","populate","populated","pored","poring","portended","portray","portrayed","portraying","portrays","pose","posed","poses","posing","position","positioned","possess","possessed","possesses","possessing","post","posted","postpone","postponed","postponing","postulate","postulated","potted","potting","pound","pounded","pounding","pour","poured","pouring","pours","pouted","powdered","power","powered","powers","practice","practiced","practices","practicing","practised","practising","prai","praise","praised","praises","praising","prancing","pray","prayed","praying","preach","preached","preaches","preaching","prearranged","precede","preceded","precedes","preceding","preceeded","preceeding","precipitated","precipitating","preclude","precluded","preconceived","preconditioned","precooked","precut","predestined","predetermined","predict","predicted","predicting","predicts","predigested","predisposed","predominated","predominates","predominating","preening","prefabricated","prefaced","prefer","preferred","preferring","prefers","prefuh","preisolated","prejudged","prejudice","prejudiced","preoccupied","preoccupies","prepackaged","prepare","prepared","prepares","preparing","preponderating","preprepared","preprinting","presage","presaged","prescribe","prescribed","prescribes","present","presented","presenting","presents","preserve","preserved","preserves","preserving","preside","presided","presides","presiding","press","pressed","presses","pressing","pressure","presume","presumed","presumes","presuming","presuppose","presupposed","presupposes","pretend","pretended","pretending","pretends","prevail","prevaile","prevailed","prevailing","prevails","prevayle","prevent","prevented","preventing","prevents","preying","price","priced","pricing","prick","pricked","pricking","pride","prides","primed","priming","primping","print","printed","printing","prize","prized","probe","probed","probing","proceed","proceeded","proceeding","proceeds","process","processed","processing","proclaim","proclaimed","proclaiming","proclaims","procrastinate","procure","procured","prod","prodded","prodding","produce","produced","produces","producing","profess","professed","professes","professing","proffered","profit","profited","program","programed","programing","programmed","programming","progress","progressed","progresses","progressing","prohibit","prohibited","prohibiting","prohibits","project","projected","projecting","projects","proliferated","prolong","prolonged","prolonging","prolongs","promise","promised","promises","promising","promote","promoted","promotes","promoting","prompt","prompted","prompts","promulgated","promulgating","pronounce","pronounced","pronouncing","prop","propagate","propagated","propel","propelled","propelling","prophesied","prophesies","propitiate","propose","proposed","proposes","proposing","propositioned","propped","propping","prorate","proscribe","proscribed","prosecute","prosecuted","prosecuting","proselytizing","prosper","prospered","prospering","prospers","prossed","prostitute","protect","protected","protecting","protects","protest","protested","protesting","protests","protracted","protrude","protruded","protruding","provdied","prove","proved","proven","proves","provide","provided","provides","providing","proving","provisioned","provoke","provoked","provokes","prowl","prowled","prowling","pruned","pry","prying","publicized","publicizing","publish","published","publishes","publishing","puckered","puckering","puff","puffed","puffing","puffs","pull","pulled","pulling","pulls","pulsating","pulse","pulsed","pulsing","pulverized","pulverizing","pummeled","pump","pumped","pumping","punch","punched","punching","punctuated","punctured","puncturing","punish","punished","punishes","punishing","punnished","punted","pupated","pupates","purchase","purchased","purchases","purchasing","purge","purged","purges","purging","purified","purify","purifying","purled","purling","purloined","purpling","purport","purported","purporting","purports","purposed","purring","pursed","pursue","pursued","pursues","pursuing","push","pushed","pushes","pushing","put","puts","putt","putted","puttering","putting","puzzle","puzzled","puzzling","pyramid"]

def sing_sen_maker():
    '''Makes a random sentence from the different parts of speech. Uses a SINGULAR subject'''
    #if input("Would you like to add a new word?").lower() == "yes":
    #    new_word = input("Please enter a singular noun.")
    #    s_nouns.append(new_word)
    #else:
    print random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)

def sealeyNewtonGen():
    for i in range(random.choice(range(1,10))):
        print random.choice(nouns['p']) + " " + random.choice(verbs['p'])

#sing_sen_maker()
#sealeyNewtonGen()
