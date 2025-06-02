import React, { useState, useEffect } from "react";
import { Box, Text, VStack, Spinner, Alert, AlertIcon, Link } from "@chakra-ui/react";
import { apiService } from "../services/api";
import { Bachelor } from "../types";

const BachelorBlock: React.FC = () => {
    const [bachelors, setBachelors] = useState<Bachelor[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchBachelors = async () => {
            try {
                setLoading(true);
                const data = await apiService.getBachelors();
                setBachelors(data);
                setError(null);
            } catch (err) {
                setError("학사공지 데이터를 불러올 수 없습니다");
            } finally {
                setLoading(false);
            }
        };

        fetchBachelors();
    }, []);

    if (loading) {
        return (
            <Box p={6} textAlign="center">
                <Spinner size="lg" color="brand.500" />
                <Text mt={4}>학사공지 로딩 중...</Text>
            </Box>
        );
    }

    if (error) {
        return (
            <Alert status="error">
                <AlertIcon />
                {error}
            </Alert>
        );
    }

    return (
        <Box bg="white" borderRadius="lg" shadow="md" p={6} h="600px" overflowY="auto">
            <Text fontSize="lg" fontWeight="bold" mb={4} color="brand.600">
                📋 학사공지
            </Text>
            <VStack spacing={3} align="stretch">
                {bachelors.length === 0 ? (
                    <Text color="gray.500" textAlign="center">
                        등록된 학사공지가 없습니다
                    </Text>
                ) : (
                    bachelors.map((bachelor) => (
                        <Link
                            key={bachelor.not_id}
                            href={bachelor.not_url}
                            isExternal
                            _hover={{ textDecoration: "none" }}
                        >
                            <Box
                                p={5}
                                bg="white"
                                borderRadius="xl"
                                border="1px"
                                borderColor="gray.100"
                                shadow="sm"
                                cursor="pointer"
                                transition="all 0.2s ease"
                                _hover={{
                                    shadow: "lg",
                                    transform: "translateY(-2px)",
                                    borderColor: "brand.200",
                                    bg: "gray.50",
                                }}
                            >
                                <Text
                                    fontWeight="600"
                                    mb={2}
                                    fontSize="sm"
                                    color="gray.800"
                                    // noOfLines={2}
                                    lineHeight="1.4"
                                >
                                    {bachelor.not_title}
                                </Text>
                                <Text fontSize="xs" color="gray.500" fontWeight="500">
                                    {bachelor.not_date}
                                </Text>
                            </Box>
                        </Link>
                    ))
                )}
            </VStack>
        </Box>
    );
};

export default BachelorBlock;
