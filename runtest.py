"""Test file for chatbot - testing both sentiment analysis and chatbot responses."""

import os
import sentiment
import chatbot


def test_sentiment_analysis():
    """Test sentiment analysis function"""
    print("\n" + "="*60)
    print("TESTING SENTIMENT ANALYSIS")
    print("="*60)
    
    test_cases = [
        ("I love this service!", "Positive"),
        ("This is terrible and awful", "Negative"),
        ("The service is okay", "Neutral"),
        ("Amazing experience! Very happy!", "Positive"),
        ("Disappointed with the quality", "Negative"),
        ("It works fine", "Neutral"),
        ("Worst service ever!", "Negative"),
        ("Excellent! Best service!", "Positive")
    ]
    
    passed = 0
    failed = 0
    
    for i, (text, expected) in enumerate(test_cases, 1):
        result = sentiment.get_sentiment(text)
        actual = result['sentiment']
        
        if actual == expected:
            print(f"[PASS] Test {i}: '{text}' -> {actual}")
            passed += 1
        else:
            print(f"[FAIL] Test {i}: '{text}' -> Expected: {expected}, Got: {actual}")
            failed += 1
    
    print(f"\nSentiment Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_conversation_analysis():
    """Test overall conversation sentiment"""
    print("\n" + "="*60)
    print("TESTING CONVERSATION ANALYSIS")
    print("="*60)
    
    messages1 = [
        "I'm very happy!",
        "Great service!",
        "Excellent work!"
    ]
    result1 = sentiment.analyze_conversation(messages1)
    test1 = result1['sentiment'] == 'Positive'
    print(f"[{'PASS' if test1 else 'FAIL'}] Test 1: Positive conversation -> {result1['sentiment']}")
    
    messages2 = [
        "This is bad",
        "Not satisfied",
        "Terrible experience"
    ]
    result2 = sentiment.analyze_conversation(messages2)
    test2 = result2['sentiment'] == 'Negative'
    print(f"[{'PASS' if test2 else 'FAIL'}] Test 2: Negative conversation -> {result2['sentiment']}")
    
    messages3 = []
    result3 = sentiment.analyze_conversation(messages3)
    test3 = result3 is None
    print(f"[{'PASS' if test3 else 'FAIL'}] Test 3: Empty conversation -> {'None' if test3 else result3}")
    
    passed = sum([test1, test2, test3])
    failed = 3 - passed
    
    print(f"\nConversation Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_chatbot_responses():
    
    if not os.path.exists('chatbot_model.pkl'):
        print()
        return 0, 0
    
    test_cases = [
        "Hello there",
        "Goodbye",
        "Thanks for your help",
        "I need help",
        "This is terrible",
        "Amazing service!",
        "Who are you?",
        "Your service is bad",
        "Great job!",
        "See you later"
    ]
    
    passed = 0
    
    for i, text in enumerate(test_cases, 1):
        response = chatbot.get_response(text)
        if response and len(response) > 0:
            print(f"[PASS] Test {i}: '{text}' -> '{response}'")
            passed += 1
        else:
            print(f"[FAIL] Test {i}: '{text}' -> No response")
    
    failed = len(test_cases) - passed
    print(f"\nChatbot Tests: {passed} passed, {failed} failed")
    return passed, failed


def test_sentiment_edge_cases():
    """Test edge cases for sentiment"""
    print("\n" + "="*60)
    print("TESTING EDGE CASES")
    print("="*60)
    
    result1 = sentiment.get_sentiment("")
    test1 = 'sentiment' in result1
    print(f"[{'PASS' if test1 else 'FAIL'}] Test 1: Empty string handling")
    
    long_text = "great " * 100
    result2 = sentiment.get_sentiment(long_text)
    test2 = result2['sentiment'] == 'Positive'
    print(f"[{'PASS' if test2 else 'FAIL'}] Test 2: Long text -> {result2['sentiment']}")
    
    result3 = sentiment.get_sentiment("12345")
    test3 = 'sentiment' in result3
    print(f"[{'PASS' if test3 else 'FAIL'}] Test 3: Numbers only handling")
    
    result4 = sentiment.get_sentiment("@#$%^&*()")
    test4 = 'sentiment' in result4
    print(f"[{'PASS' if test4 else 'FAIL'}] Test 4: Special characters handling")
    
    result5 = sentiment.get_sentiment("I love it but also hate it")
    test5 = 'sentiment' in result5
    print(f"[{'PASS' if test5 else 'FAIL'}] Test 5: Mixed sentiment -> {result5['sentiment']}")
    
    passed = sum([test1, test2, test3, test4, test5])
    failed = 5 - passed
    
    print(f"\nEdge Case Tests: {passed} passed, {failed} failed")
    return passed, failed


def main():
    """Run all tests"""
    print("\n" + "="*70)
    print("CHATBOT TESTING SUITE")
    print("="*70)
    
    total_passed = 0
    total_failed = 0
    
    p1, f1 = test_sentiment_analysis()
    total_passed += p1
    total_failed += f1
    
    p2, f2 = test_conversation_analysis()
    total_passed += p2
    total_failed += f2
    
    p3, f3 = test_chatbot_responses()
    total_passed += p3
    total_failed += f3
    
    p4, f4 = test_sentiment_edge_cases()
    total_passed += p4
    total_failed += f4
    
   
    
    print("\n" + "="*70)
    print("FINAL RESULTS")
    print("="*70)
    print(f"Total Tests Run: {total_passed + total_failed}")
    print(f"Tests Passed: {total_passed}")
    print(f"Tests Failed: {total_failed}")
    
    if total_failed == 0:
        print("\nALL TESTS PASSED!")
    else:
        print(f"\n{total_failed} tests failed. Please check the errors above.")
    
    print("="*70)


if __name__ == "__main__":
    main()
