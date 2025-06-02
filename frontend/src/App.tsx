import React from "react";
import { Box, Container, Grid, GridItem, Text, VStack, Link } from "@chakra-ui/react";
import CheeringMessage from "./components/CheeringMessage";
import DigitalClock from "./components/DigitalClock";
import BachelorBlock from "./components/BachelorBlock"; // 새로 추가
import EventsBlock from "./components/EventsBlock";
import CrawlingButton from "./components/CrawlingButton";

const App: React.FC = () => {
    return (
        <Box minH="100vh" bg="gray.100" py={8}>
            <Container maxW="6xl">
                <CheeringMessage />

                <DigitalClock />

                <VStack spacing={4} mb={10} p={6} align="start" bg="gray.100" borderRadius="xl">
                    <Box display="flex" alignItems="center" gap={3}>
                        <Text fontSize="2xl" fontWeight="bold" color="black">
                            금오광장
                        </Text>
                        <Link href="https://www.kumoh.ac.kr/ko/sub06_01_01_01.do" isExternal>
                            <Box
                                mt={1}
                                bg="green.600"
                                color="white"
                                px={3}
                                py={1}
                                borderRadius="full"
                                fontSize="xs"
                                fontWeight="medium"
                                _hover={{ bg: "green.700" }}
                                transition="all 0.2s ease"
                            >
                                바로가기 →
                            </Box>
                        </Link>
                    </Box>
                    <Grid templateColumns="1fr 1fr" gap={6} w="100%" h="500px" mb={4}>
                        <GridItem>
                            <BachelorBlock />
                        </GridItem>
                        <GridItem>
                            <EventsBlock />
                        </GridItem>
                    </Grid>
                </VStack>
            </Container>

            <CrawlingButton />
        </Box>
    );
};

export default App;
