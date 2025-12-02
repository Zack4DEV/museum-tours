import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import MuseumAIGuide from '../components/MuseumAIGuide';

const AIGuideScreen = () => {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Museum AI Guide</Text>
        <Text style={styles.subtitle}>
          Ask me anything about exhibits, artwork, or museum information
        </Text>
      </View>
      <View style={styles.guideContainer}>
        <MuseumAIGuide />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    padding: 16,
    backgroundColor: '#f8f8f8',
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
  guideContainer: {
    flex: 1,
  },
});

export default AIGuideScreen;
