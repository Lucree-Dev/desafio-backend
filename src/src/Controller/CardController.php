<?php

namespace App\Controller;

use App\Service\Card as ServiceCard;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\SerializerInterface;

class CardController extends AbstractController
{
    /** SerializerInterface */
    private $serializer;
    /** @var ServiceCard */
    private $service;

    public function __construct(
        ServiceCard $serviceCard,
        SerializerInterface $serializer
        )
    {
        $this->serializer = $serializer;
        $this->service = $serviceCard;    
    }

    /**
     * @Route("/card", name="card_list", methods="GET")
     */
    public function index()
    {
        $response = new JsonResponse();
        $response->setContent(
            $this->serializer->serialize(
                $this->service->list(),
                'json'
            )
        );
        return $response;
    }

    /**
     * @Route("/card", name="card_create", methods="POST")
     */
    public function create(Request $request)
    {
        $data = $request->request->all();
        $card = $this->service->create($data);
        $response = new JsonResponse();
        $response->setContent(
            $this->serializer->serialize(
                $card,
                'json'
            )
        );
        return $response;
    }
}
