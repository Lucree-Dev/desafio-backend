<?php

namespace App\Controller;

use App\Service\Person as ServicePerson;
use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\Routing\Annotation\Route;
use Symfony\Component\Serializer\SerializerInterface;

class PersonController extends AbstractController
{
    /** SerializerInterface */
    private $serializer;
    /** @var ServicePerson */
    private $service;

    public function __construct(
        ServicePerson $servicePerson,
        SerializerInterface $serializer
        )
    {
        $this->serializer = $serializer;
        $this->service = $servicePerson;    
    }

    /**
     * @Route("/person", name="person_list", methods="GET")
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
     * @Route("/person", name="person_create", methods="POST")
     */
    public function create(Request $request)
    {
        $data = $request->request->all();
        $person = $this->service->create($data);
        $response = new JsonResponse();
        $response->setContent(
            $this->serializer->serialize(
                $person,
                'json'
            )
        );
        return $response;
    }
}
