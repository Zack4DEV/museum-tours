import { Tabs } from 'expo-router';
import { MaterialIcons } from '@expo/vector-icons';

export default function AppLayout() {
  return (
    <Tabs screenOptions={{
      tabBarActiveTintColor: '#2c3e50',
      tabBarInactiveTintColor: '#95a5a6',
      headerStyle: {
        backgroundColor: '#2c3e50',
      },
      headerTintColor: '#fff',
    }}>
      <Tabs.Screen
        name="explore"
        options={{
          title: 'Explore',
          tabBarIcon: ({ color }) => (
            <MaterialIcons name="explore" size={24} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="tours"
        options={{
          title: 'Tours',
          tabBarIcon: ({ color }) => (
            <MaterialIcons name="map" size={24} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="exhibits"
        options={{
          title: 'Exhibits',
          tabBarIcon: ({ color }) => (
            <MaterialIcons name="museum" size={24} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="ai-guide"
        options={{
          title: 'AI Guide',
          tabBarIcon: ({ color }) => (
            <MaterialIcons name="chat" size={24} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Profile',
          tabBarIcon: ({ color }) => (
            <MaterialIcons name="person" size={24} color={color} />
          ),
        }}
      />
    </Tabs>
  );
}