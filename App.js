// App.js
import React from 'react';
import { Button, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
const Stack = createStackNavigator();
function HomeScreen({ navigation }) {
return (
<View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
<Text>Bem-vindo ao Meu App de navegação!</Text>
<Button title="Próxima tela :)" onPress={() => navigation.navigate('Perfil')} />
</View>
);
}
function PerfilScreen() {
return (
<View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
<Text>Segunda telaa :|</Text>
</View>
);
}
export default function App() {
return (
<NavigationContainer>
<Stack.Navigator initialRouteName="Home">
<Stack.Screen name="Home" component={HomeScreen} />
<Stack.Screen name="Perfil" component={PerfilScreen} />
</Stack.Navigator>
</NavigationContainer>
);
}
