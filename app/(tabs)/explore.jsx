import React from 'react';
import {
  View,
  Text,
  ScrollView,
  StyleSheet,
  TouchableOpacity,
  Image,
} from 'react-native';
import { MaterialIcons } from '@expo/vector-icons';
import { tours } from '../data/tours';
import { categories } from '../data/exhibits';

const ExploreScreen = () => {
  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.headerTitle}>Welcome to the Museum</Text>
        <Text style={styles.headerSubtitle}>Discover art, history, and science</Text>
      </View>

      {/* Featured Tours */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Featured Tours</Text>
        <ScrollView horizontal showsHorizontalScrollIndicator={false}>
          {tours.map((tour) => (
            <TouchableOpacity key={tour.id} style={styles.tourCard}>
              <Image source={{ uri: tour.image }} style={styles.tourImage} />
              <View style={styles.tourInfo}>
                <Text style={styles.tourTitle}>{tour.title}</Text>
                <Text style={styles.tourDuration}>{tour.duration}</Text>
                <View style={styles.tourRating}>
                  <MaterialIcons name="star" size={16} color="#FFD700" />
                  <Text style={styles.ratingText}>{tour.rating}</Text>
                </View>
              </View>
            </TouchableOpacity>
          ))}
        </ScrollView>
      </View>

      {/* Categories */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Categories</Text>
        <View style={styles.categoriesGrid}>
          {categories.map((category) => (
            <TouchableOpacity key={category.id} style={styles.categoryCard}>
              <View
                style={[
                  styles.categoryIconContainer,
                  { backgroundColor: category.color },
                ]}
              >
                <MaterialIcons
                  name={category.icon}
                  size={24}
                  color="#fff"
                />
              </View>
              <Text style={styles.categoryName}>{category.name}</Text>
            </TouchableOpacity>
          ))}
        </View>
      </View>
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f8f8f8',
  },
  header: {
    padding: 24,
    backgroundColor: '#2c3e50',
  },
  headerTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    color: '#fff',
    marginBottom: 4,
  },
  headerSubtitle: {
    fontSize: 16,
    color: '#bdc3c7',
  },
  section: {
    padding: 16,
  },
  sectionTitle: {
    fontSize: 20,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  tourCard: {
    backgroundColor: '#fff',
    borderRadius: 12,
    marginRight: 16,
    width: 250,
    overflow: 'hidden',
    elevation: 2,
  },
  tourImage: {
    width: '100%',
    height: 120,
  },
  tourInfo: {
    padding: 12,
  },
  tourTitle: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  tourDuration: {
    fontSize: 14,
    color: '#666',
    marginBottom: 4,
  },
  tourRating: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  ratingText: {
    marginLeft: 4,
    fontSize: 14,
    color: '#333',
  },
  categoriesGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  categoryCard: {
    width: '48%',
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    alignItems: 'center',
    marginBottom: 16,
    elevation: 2,
  },
  categoryIconContainer: {
    width: 60,
    height: 60,
    borderRadius: 30,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 8,
  },
  categoryName: {
    fontSize: 16,
    fontWeight: '600',
  },
});

export default ExploreScreen;
