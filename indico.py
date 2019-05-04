import os
import cv2 as cv
import indicoio

from indicoio.custom import Collection
indicoio.config.api_key = 'bb2ce29a2086bceb98bc297f6a961656'

def generate_training_data(fname):
    """
    Read in text file and generate training data.
    Each line looks like the following:

    1050: [1, 2, 3, 4, 5]
    1349: [1, 2, 3, 4, 5]
    4160: [1, 2, 3]
    ...

    First we split on the colon of each row, where the first
    half is the image filename and the second half is its
    associated labels.
    """
    with open(fname) as f:
        for line in f:
            shirt, targets = line.split(":")
            shirt_path = "my_training_shirts/{image}.jpg".format(
                image=shirt.strip()
            )
            shirt_path = os.path.abspath(shirt_path)

            # parse out the list of targets
            target_list = targets.strip()[1:-1].split(",")
            labels = map(lambda target: "label" + target.strip(), target_list)
            yield [ (shirt_path, label) for label in labels]
    raise StopIteration


if __name__ == "__main__":
    collection = Collection("clothes_collection_1")

    # Clear any previous changes
    try:
        collection.clear()
    except:
        pass

    train = generate_training_data("clothes_match_labeled_data.txt")

    total = 0
    for samples in train:
        print("Adding {num} samples to collection".format(num=len(samples)))
        collection.add_data(samples)
        total += len(samples)
        print("Added {total} samples to collection thus far".format(total=total))

    collection.train()
    collection.wait()
    img = cv.imread("test_shirts/12770.jpg")

    collection = Collection("clothes_collection_1")
    predict = collection.predict(img)
    outcome = max(predict, key=predict.get)
    print(outcome)
