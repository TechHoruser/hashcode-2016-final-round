from algorithms import BaseAlgorithms
from manager_file import ManagerFile

examples = [
    {"fileName": "constellation", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "forever_alone", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "overlap", "algorithm": BaseAlgorithms.basic,},
    {"fileName": "weekend", "algorithm": BaseAlgorithms.basic,},
]


for indx, example in enumerate(examples):
    print(
        "Processing file:",
        example["fileName"],
        "(" + str(indx + 1) + "/" + str(len(examples)) + ")",
        flush=False,
    )
    mf = ManagerFile(example["fileName"])
    input_array = mf.loadFile()

    output = example["algorithm"](input_array)

    mf.saveFile([len(output), output])
