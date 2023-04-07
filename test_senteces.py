# Import global variables from 'sentences.py'
from sentences import (
    tenses,
    determiners_singular,
    determiners_plural,
    nouns_singular,
    nouns_plural,
    verbs_past,
    verbs_present_singular,
    verbs_present_plural,
    verbs_future,
    prepositions,
    get_determiner,
    get_noun,
    get_verb,
    get_preposition,
    get_prepositional_phrase,
)

import pytest

# Define amount of tests per method
test_count = 4


def test_get_determiner():
    # 1. Test the single determiners.

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(test_count):
        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in determiners_singular

    # 2. Test the plural determiners.

    # This loop will repeat the statements inside it 4 times.
    for _ in range(test_count):
        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in determiners_plural


def test_get_noun():
    # Singular noun
    for _ in range(test_count):
        # Calling get_noun() to return noun generated
        # with '1' as the parameter to return singular noun
        noun = get_noun(1)
        # Verify that the noun obtained from get_noun()
        # returns a value for singular nouns
        assert noun in nouns_singular
    # Plural noun
    for _ in range(test_count):
        # Calling get_noun() to return noun generated
        # with '0' as the parameter to return plural noun
        noun = get_noun(0)
        # Verify that the noun obtained from 'get_noun()'
        # returns a value for plural nouns
        assert noun in nouns_plural


def test_get_verb():
    # Past tense
    for _ in range(test_count):
        # Calling get_verb() to return verb generated
        # with '1' as the noun parameter and 'tenses[0]'
        # equals to 'past' to return singular verb in past tense
        verb = get_verb(1, tenses[0])
        assert verb in verbs_past
    # Present tense singular
    for _ in range(test_count):
        # Calling get_verb() to return verb generated
        # with '1' as the noun parameter and 'tenses[1]'
        # equals to 'present' to return singular verb in present tense
        verb = get_verb(1, tenses[1])
        assert verb in verbs_present_singular
    # Present tense plural
    for _ in range(test_count):
        # Calling get_verb() to return verb generated
        # with '0' as the noun parameter and 'tenses[1]'
        # equals to 'present' to return plural verb in present tense
        verb = get_verb(0, tenses[1])
        assert verb in verbs_present_plural
    # Future tense
    for _ in range(test_count):
        # Calling get_verb() to return verb generated
        # with '1' as the noun parameter and 'tenses[2]'
        # equals to 'future' to return singular verb in future tense
        verb = get_verb(1, tenses[2])
        assert verb in verbs_future


def test_get_preposition():
    for _ in range(test_count):
        # Calling get_verb() to return verb generated
        # to return a preposition
        preposition = get_preposition()
        assert preposition in prepositions


def test_get_prepositional_phrase():
    # Singular prepositional phrase
    for _ in range(test_count):
        # Calling get_verb() to return verb generated
        # with '1' as parameter to return
        # prepositional phrase with singular nouns
        prepositional_phrase = get_prepositional_phrase(1)
        assert (
            prepositional_phrase in prepositions
            or determiners_singular
            or nouns_singular
        )
    # Plural prepositional phrase
    for _ in range(test_count):
        # Calling get_verb() to return verb generated
        # with '0' as parameter to return
        # prepositional phrase with plural nouns
        prepositional_phrase = get_prepositional_phrase(0)
        assert (
            prepositional_phrase in prepositions or determiners_plural or nouns_plural
        )


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
        
