import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Row, Col, Image, ListGroup, Button, Card } from "react-bootstrap";
import axios from "axios";

function ProductScreen() {
  const { id } = useParams();
  const [product, setProduct] = useState({});

  useEffect(() => {
    async function fetchProduct() {
      try {
        const { data } = await axios.get(`/api/prod/${id}/`);
        setProduct(data);
      } catch (error) {
        console.error("Error fetching product:", error);
      }
    }

    fetchProduct();
  }, [id]);

  return (
    <div>
      <h1>{product.name}</h1>
    </div>
  );
}

export default ProductScreen;
